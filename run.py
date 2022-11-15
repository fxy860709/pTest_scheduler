from flask import Flask,render_template,request

app = Flask(__name__,template_folder='app/templates/accounts')

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/home')
# def home_page():
#     return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return request.form


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8088"), debug=True)
