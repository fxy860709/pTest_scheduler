from flask import Blueprint
from flask import Flask,render_template,request,redirect,url_for

task = Blueprint(
    'task_manage',
    __name__,
    url_prefix=''
)
@task.route('/task_manage')
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
    return render_template('pages/task_manage.html', segment='task_manage', navigation_name="任务管理", env_infos=task_infos)


# penv = Blueprint('penv',__name__)
#
# @penv.route('/list')
# def penv_list():
#     return 'penvlist'
#
# @penv.route('/add')
# def penv_add():
#     return 'penvadd'
