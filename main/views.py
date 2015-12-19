import logging
from itertools import islice

from flask import render_template
from imgurpython import ImgurClient
from requests.exceptions import ConnectionError

from FlaskTutor import app
from .models import User, Album, db

logger = logging.getLogger(__name__)

def matches_reqs(item):
    return \
        not item.is_album and \
        not item.nsfw  # and \
        # (item.ups / item.downs > 8)


@app.route('/')
def index():
    client = ImgurClient(app.config['IMGUR_ID'], app.config['IMGUR_SECRET'])
    try:
        albums = client.gallery(sort='top', window='week', page=0)
    except ConnectionError:
        logger.error('Connection error')
        return
    images = list(islice((a for a in albums if matches_reqs(a)), 0, 10))
    for img in images:
        if img.account_id:
            author = User.query.get(img.account_id)
            if not author:
                author = User(id=img.account_id, nickname=img.account_url)
                db.session.add(author)
            if not Album.query.get(img.id):
                a = Album(id=img.id, link=img.link, author=author, title=img.title)
                db.session.add(a)
    db.session.commit()

    return render_template(
        "index.html",
        images=images)


@app.route('/hello')
def hello_again():
    return 'Hello again!'

