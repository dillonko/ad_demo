from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
import sqlite3
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/userdata/', methods=["POST"])
# def form_data():
#     error = None
#     if request.method == 'POST':
#         # add validation code
#
#         jsondata = request.form['jsondata']
#         data = json.loads(jsondata)
#
#         #should return somthing
#         return render_template('request.html', data=data, jsondata=jsondata)
#
#     else:
#         return "fail"

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'example.db'),
    DEBUG=True
))

def connect_db():
    """connect to the specific db"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """opens a new db connection if there is none yet for the cyrrent app"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """closes the db again at the end of the request."""
if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

@app.route('/save', methods=['PUT','POST'])
def get_info():
  print ("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(id,
                                                                 firstname,
                                                                 lastname,
                                                                 youremail,
                                                                 title,
                                                                 managersemail,
                                                                 startdate,
                                                                 account0,
                                                                 account1,
                                                                 account2,
                                                                 account3,
                                                                 account4,
                                                                 account5,
                                                                 account6,
                                                                 account7,
                                                                 account8,
                                                                 account9,
                                                                 account10,
                                                                 account11,
                                                                 account12,
                                                                 account13,
                                                                 account14,
                                                                 account15))


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=7000)
