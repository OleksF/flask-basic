from flask import Flask, request
app = Flask(__name__)

with open('s', 'w') as fl:
    fl.write(' ')

seed = ' '

@app.route('/',methods = ['POST', 'GET'])
def seed():
    if request.method == 'POST':
        with open('s', 'w') as fl:
            fl.write(str(request.get_json()['num']))
        return ' '
    else:
        with open('s') as fl:
            seed = fl.read()
        return seed
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)