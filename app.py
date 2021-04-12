# A very simple Flask Hello World app for you to get started with...
from PIL import Image
from flask import Flask, request, jsonify, url_for
import os
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


app = Flask(__name__, static_folder='static')

host = "http://vyd2999.pythonanywhere.com"


@app.route('/', methods=["POST"])
def process_image():
    file = request.files['image']

    # creating a image object (main image)
    im1 = Image.open(file)
    name = randomword(5) + ".jpg"

    # save a image using extension
    im1 = im1.save("static/" + name)

    return jsonify({'msg': 'success', 'url': host + url_for('static', filename=name)})


if __name__ == '__main__':

    app.run(threaded=True)
