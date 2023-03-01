from flask import Blueprint
from flask import Flask,render_template,request,redirect,url_for

case = Blueprint(
    'case_manage',
    __name__,
    url_prefix=''
)
@case.route('/case_manage')
def task_manage_index():
    task_infos = [
        {
            "id": 1,
            "env_id": 123,
            "env_ip": "1.1.1.1",
            "env_cmc_dir": "/home/tools/cmc",
            "env_manual": "V2环境"

        },
        {
            "id": 1,
            "env_id": 123,
            "env_ip": "1.1.1.1",
            "env_cmc_dir": "/home/tools/cmc",
            "env_manual": "V3环境"
        },
        {
            "id": 1,
            "env_id": 123,
            "env_ip": "1.1.1.1",
            "env_cmc_dir": "/home/tools/cmc",
            "env_manual": "V4环境"

        }
    ]
    return render_template('pages/case_manage.html', segment='index', env_infos=task_infos)

    # return render_template('pages/env_manage.html', segment='index', navigation_name="环境管理", env_infos='env_infos')

# penv = Blueprint('penv',__name__)
#
# @penv.route('/list')
# def penv_list():
#     return 'penvlist'
#
# @penv.route('/add')
# def penv_add():
#     return 'penvadd'
