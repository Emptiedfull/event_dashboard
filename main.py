import flask
import requests
import os


app = flask.Flask(__name__,static_folder='build',static_url_path='/')


@app.route('/info')
def get_info():
    response = requests.get('http://3.7.45.71:7777/get_all?key=account').json()
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return flask.send_from_directory(app.static_folder, path)
    else:
        return flask.send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
    