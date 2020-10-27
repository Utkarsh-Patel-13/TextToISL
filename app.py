from flask import Flask, render_template, redirect
from flask_cors import CORS
from flask import request
from engtoisl import convert_sentence

from googletrans import Translator

app = Flask(__name__)
cors = CORS(app=app)

@app.route('/', methods=['GET'])
@app.route('/<f_name>/', methods=['GET'])
def index(f_name: str = None):
    path = "../static/videos/alphabets.mp4"
    if f_name is not None:
        path = "../static/videos/" + f_name
    return render_template('index.html', path=path)


@app.route('/api/convert', methods=['POST'])
def convert():
    # data = request.json

    # inp = data["input"]
    # print(inp)

    # path = convert_sentence(inp)

    # return {
    #     "path": path
    # }
    if request.method == 'POST':
        data = request.form.to_dict()
        
        translate = Translator()
        t = translate.translate(data["inputBox"])

        path = convert_sentence(t.text)

        if path is None:
            path = 'alphabets.mp4'

        return redirect('/' + path, )



if __name__ == "__main__":
    app.run(debug=True)