from flask import Flask,render_template,request,redirect

app = Flask(__name__,template_folder='app/templates/accounts')

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/home')
# def home_page():
#     return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = "输入错误"
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if user == 'fxy' and password == '123':
            return redirect ('/home')
        else:
            return render_template('login.html',login_error=error)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8088"), debug=True)
