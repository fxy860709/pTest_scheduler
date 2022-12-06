from flask import Blueprint

parse_json=Blueprint('parse_json',__name__)

@parse_json.route('/parse')
def parse():
    return 'parse_json'