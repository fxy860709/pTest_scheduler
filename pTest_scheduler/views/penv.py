from flask import Blueprint
from flask import Flask,render_template,request,redirect,url_for

# penv = Blueprint('penv',__name__)
#
# @penv.route('/list')
# def penv_list():
#     return 'penvlist'
#
# @penv.route('/add')
# def penv_add():
#     return 'penvadd'

penv = Blueprint(
    'env_manage',
    __name__,
    url_prefix=''
)

@penv.route('/list')
def env_manage_index():
    # return 'penvlist'
    # return render_template('account/login.html')
    return render_template('accounts/env_manage.html', segment='index', navigation_name="环境管理", env_infos='env_infos')
