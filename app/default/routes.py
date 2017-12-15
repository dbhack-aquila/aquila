from . import default

@default.route('/')
def home():
    return default.send_static_file('index.html')


@default.route('/test')
def test():
    return default.send_static_file('../test_paul/test.html')


