from flask import Flask,request,jsonify


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return "hello"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)