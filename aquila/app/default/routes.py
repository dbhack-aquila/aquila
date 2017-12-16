from . import default


@default.route('/')
def home():
    return default.send_static_file('index.html')


@default.route('/test')
def test():
    return default.send_static_file('test_paul/test.html')

@default.route('/train.js')
def train():
    return default.send_static_file('test_paul/train.js')
@default.route('/DerKleineICE.png')
def png():
    return default.send_static_file('test_paul/DerKleineICE.png')

#@default.route('/test')
#@default.route('/test/<path:path>')
#def send_sites(path='test.html'):
#    return default.send_from_directory('test_paul', path)