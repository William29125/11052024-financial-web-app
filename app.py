from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["Get" , "Post"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["Get" , "Post"])
def main():
    r = request.form.get("q")
    return(render_template("main.html",r=r))
    
if __name__=="__main__":
   app.run()
