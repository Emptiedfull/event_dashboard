import flask
import requests
from flask_cors import CORS




app = flask.Flask(__name__,static_folder='build',static_url_path='/static')
CORS(app)



@app.route('/info')
def get_info():
    response = requests.get('http://3.7.45.71:7777/get_all?key=account').json()
    return response

if __name__ == '__main__':
    app.run(debug=True)
    