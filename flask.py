from flask import Flask
app= flask.Flask(__name__)
def hello():
    return 'HELLO'
if __name__=='HELLO':
    app.run()