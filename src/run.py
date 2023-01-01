from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from main import callFunc
# val = callFunc()
# print(val)


app = Flask(__name__)
CORS(app)


@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        image = request.files['image']
        image.save(f"../Image1.png")
        val = callFunc()
        print(val)
        return make_response(jsonify(word=val[0], probabity=f"value : {int(val[1]*100)}%"))
    except Exception as e:
        print(e, e.__traceback__.tb_lineno)
        return make_response(jsonify(error="Some error Occurec"))


@app.route('/', methods=['POST', 'GET'])
def GET():

    return "hehe perfect"


if __name__ == '__main__':
    app.run(debug=True)
