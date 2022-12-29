from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder='template')

@app.route('/', methods = ['POST', 'GET'])
def home(): 
     if request.method == 'POST':
         return render_template('index.html')
     else:
         return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
      return render_template('login.html')
    else:
      return render_template('login.html')

@app.route('/thx',methods = ['POST', 'GET'])
def thx():
    if request.method == 'POST':
      user = request.form["nm"]
      return render_template('thx.html', user = user)
    else:
      return render_template('thx.html')

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port='5000',debug=True)