from flask import Flask, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def seed():
    if request.method == 'POST':
        with open('s', 'w') as fl:
            fl.write(request.get_json()['num'])
    else:
        with open('s') as fl:
            seed = int(fl.read())
        return seed
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)