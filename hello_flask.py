from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello man'

if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=80, debug=True)
#kkkkkkkk執行專案，程式會告知你連結網址