from flask import Flask, request
import json

def write(file,data):
    with open(file,"w",encoding="UTF-8") as f:
        json.dump(data,f)

app = Flask(__name__)





@app.route("/gfshjoifhugih/iidshfidhdfioidd/rrr345u8939f5876438dw/fcwef123",methods=["POST"])
def geter():
    write("test.json",request.json)
    return "1"

@app.route("/gfshjoifhugih/iidshfidhdfioidd/rrr345u8939f5876438dw/fcwef123/qaz",methods=["POST"])
def geewq():
    write("files.json",request.json)
    return "1"

app.run(host="0.0.0.0", debug=True)