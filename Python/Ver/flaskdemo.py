from flask import Flask
from flask import Response

#run
# $env:FLASK_APP = "flaskdemo"
# flask run -h localhost -p 3000


app = Flask(__name__)

@app.route('/content/<path:file>')
def projects(file):
    with open(file, "r", encoding='utf-8') as f:
        contetd = f.read()
    return Response(contetd, status=200, mimetype='application/json')
#http://127.0.0.1:3000/content/F:/temp/words.txt

@app.route('/register/<path:file>')
def about(file):
    with open(file, 'w') as newfile:
      newfile.write("hello")
    return Response("success", status=201, mimetype='application/json')

#http://127.0.0.1:3000/register/F:/temp/words2.txt
