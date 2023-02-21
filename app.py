import pyshorteners
from flask import Flask, request, render_template

app = Flask(__name__)

# anasayfa
@app.route("/")
def homepage():
    try:
        return render_template("index.html")

    except:
        return render_template("error.html")

# kısaltma link
@app.route("/shorten", methods=['POST', 'GET'])
def convert():
    try:
        url = None
        tinylink = None
        
        if request.method == "POST":
            url = request.form.get("url")
            s = pyshorteners.Shortener()
            tinylink = s.tinyurl.short(url)

            return render_template("shorten.html", tinylink = tinylink, url = url)
        
        else:
            pass
            
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)

