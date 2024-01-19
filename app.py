from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "my first ml project-1"

if __name__=="__main__":
    app.run(debug=True)