from aquila.app.default.point_of_interest_api import get_point_of_interest_json
from aquila.app.default.ice_portal_api import get_status, get_trip_info
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/gps/<float:train_latitude>/<float:train_longitude>')
def point_of_interest_api(train_latitude, train_longitude):
    return get_point_of_interest_json(train_latitude, train_longitude)

@app.route('/api1/rs/status')
def ice_portal_status_api():
    return jsonify(dict(get_status()))

@app.route('/api1/rs/tripInfo')
def ice_portal_trip_info_api():
    return jsonify(dict(get_trip_info()))


@app.route('/')
@app.route('/<path:file_path>')
def default_route(file_path='index.html'):
    return send_from_directory('app/static/dist', file_path)


if __name__ == '__main__':
    app.run(debug=True)
