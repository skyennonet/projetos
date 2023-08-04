from flask import Flask

app = Flask(__name__)
@app.route("/")
def homepage():
    return "esse é meu primeiro site!!!"


#colocar o site no ar
#app.run