from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello man'

if __name__ == '__main__':
    app.debug = True
    #app.run(aaaaaaaaaaa) 
    app.run(host='0.0.0.0', port=80, debug=True)

 