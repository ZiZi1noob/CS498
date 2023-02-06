from flask import Flask, request
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def hello():
    global seed
    if(request.method == 'POST'):
        seed = request.json['num']
        return jsonify({"num": seed})
    elif(request.method == 'GET'):
        return str(seed)

if __name__ ==  '__main__':
    app.run(host='0.0.0.0',port = 5000)
