from flask import Flask,render_template,request,redirect

# 创建flask对象
app = Flask(__name__,template_folder='app/templates/accounts')
# 存储数据
Data_dict = {
    1: {'name':'v3','ip':'1.1.1.1'},
    2: {'name':'v2','ip':'2.2.2.2'}
}


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

@app.route('/env_list')
def register_env():
    # data_dict=Data_dict
    return render_template('env_list.html', data_dict=Data_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8088"), debug=True)
