from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/userdata/', methods=["POST"])
def form_data():
    error = None
    if request.method == 'POST':
        # add validation code

        print(request.form)

        #should return somthing
        return "success"

    else:
        return "fail"

if __name__ == "__main__":
    app.run()
