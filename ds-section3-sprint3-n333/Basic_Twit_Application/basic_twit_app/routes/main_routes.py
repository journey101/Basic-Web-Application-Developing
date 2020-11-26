from flask import jsonify
from flask import Blueprint, render_template
from basic_twit_app.models import Users, parse_records

main_routes = Blueprint('main_routes', __name__)

# '/'
@main_routes.route('/')
def index():
    return render_template("index.html")

# '/menu.json
@main_routes.route('/menu.json')
def json_data():
    raw_data = Users.query.all()
    parsed_data = parse_records(raw_data)

    return jsonify(parsed_data)