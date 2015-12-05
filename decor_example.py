def skimmer(decorated, *args, **kwargs):
    print("Decorator called")

    def caller(*args2, **kwargs2):
        print("Intercepted args: {}'".format(args2))
        print("Intercepted kwargs: {}'".format(kwargs2))
        decorated(*args2, message="Skimmer", **kwargs2)

    return caller


def repeater(decorated):
    def caller(*args, **kwargs):
        for i in range(5):
            res = decorated(*args, **kwargs)
            if res:
                return res

    return caller


def get_data():
    print("get_data()")
    response = requests.get('http://wikipedia.org')
    if response.status_code != 200:
        return

    print(len(response.content))


@skimmer
def bankomat(pin, message=None):
    print("Pin: {}".format(pin))
    if message:
        print("Message: {}".format(message))


