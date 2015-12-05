import logging
from itertools import islice

from FlaskTutor import app
from flask import render_template
from requests.exceptions import ConnectionError
from imgurpython import ImgurClient

from .models import User, Album, db

logger = logging.getLogger(__name__)

IMGUR_ID = "xxx"
IMGUR_SECRET = "yyy"


def matches_reqs(item):
    return \
        not item.is_album and \
        not item.nsfw  # and \
        # (item.ups / item.downs > 8)


@app.route('/')
def index():
    client = ImgurClient(IMGUR_ID, IMGUR_SECRET)
    try:
        gallery = client.gallery(sort='top', window='week', page=0)
    except ConnectionError:
        logger.error('Connection error')
        return
    images = list(islice((item for item in gallery if matches_reqs(item)), 0, 10))
    for i in images:
        if i.account_id:
            author = User.query.get(i.account_id)
            if not author:
                author = User(id=i.account_id, nickname=i.account_url)
                db.session.add(author)
            if not Album.query.get(i.id):
                a = Album(id=i.id, link=i.link, author=author)
                db.session.add(a)
    db.session.commit()

    return render_template(
        "index.html",
        images=images)


@app.route('/hello')
def hello_again():
    return 'Hello again!'

