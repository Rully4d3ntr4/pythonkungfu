<<<<<<< HEAD
from flask import Flask
from flask import render_template
from flask import Response

app = Flask('webapp')


def plain(text):
    return Response(
        response=text,
        status=200,
        headers=None,
        mimetype='application/x-javascript',
        content_type=None,
        direct_passthrough=False
    )
=======
#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request
import urllib


app = Flask('webapp')
>>>>>>> d47bff5a72b8f713337dc7f1cd796179d0619e7e


@app.route("/")
def index():
<<<<<<< HEAD
    json = {
        "greet": "Holla",
        "name": "blusp10it"
    }
    return render_template('index.html', data=json)


@app.route("/hello")
def hello():
    return plain("Hello world!")

if __name__ == "__main__":
    app.run(debug=True)
=======
    return render_template('index.html')


@app.route("/", methods=["POST"])
def post():
    datas = urllib.unquote(request.data).decode('utf8').encode('ascii', 'ignore')
    segment1 = (datas.split('&')[0]).split('=')[1]
    segment2 = (datas.split('&')[1]).split('=')[1]
    segment3 = (datas.split('&')[2]).split('=')[1]
    hasil = 0
    if segment2 == "+":
        hasil = float(segment1) + float(segment3)
        hasil = str(hasil)
    if segment2 == "-":
        hasil = float(segment1) - float(segment3)
        hasil = str(hasil)
    if segment2 == "*":
        hasil = float(segment1) * float(segment3)
        hasil = str(hasil)
    if segment2 == "/":
        hasil = float(segment1) / float(segment3)
        hasil = str(hasil)
    return hasil

if __name__ == "__main__":
    app.run()
>>>>>>> d47bff5a72b8f713337dc7f1cd796179d0619e7e
