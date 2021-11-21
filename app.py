from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    text="Subscribe to 'End to End' YouTube Channel."
    hinText="'एंड टू एंड' यूट्यूब चैनल को सब्सक्राइब करें।"
    return render_template("index.html",result=text,hresult=hinText)

if __name__=="__main__":
    app.run()
