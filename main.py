from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():

     return render_template("circuit_viewer.html")
if __name__=="__main__":

        app.run(debug=True,threaded=True,host="0.0.0.0",port=9040)

