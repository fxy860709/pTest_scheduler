from flask import Blueprint

analysis_log=Blueprint('analysis',__name__)

@analysis_log.route('/analysis')
def analysis():
    return 'analysis'