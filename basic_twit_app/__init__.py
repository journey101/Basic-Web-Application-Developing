from flask import Flask
from basic_twit_app.routes import del_routes, analytics, update_routes, main_routes, add_routes, users_routes
from basic_twit_app.models import db, migrate

#elephansql(postgreSQL) URI로 적용하기. 
# DATABASE_URI = f"postgres://cpkfkuik:98SilJDjsuv4vcUDe-tWbeNbqqMOGukm@john.db.elephantsql.com:5432/cpkfkuik"

# DATABASE_URI = f"postgres://abilwzqo:P39FFfs888U_dH0IV9T9p9hK1wsBSQyk@john.db.elephantsql.com:5432/abilwzqo"

# DATABASE_URI = f"postgres://cdfpqaqk:NYBpbU95K63_YL5CgvBCU77hkVha-mA8@john.db.elephantsql.com:5432/cdfpqaqk"
# DATABASE_URI = "sqlite:///twitter.sqlite3"
DATABASE_URI = "postgres://cvzxsdflogngqw:4b1668e1635061d065ce10f7309f8c5a17ab5fa39353758bcc27691124b8c0a0@ec2-52-206-44-27.compute-1.amazonaws.com:5432/d899d99bbdlr5u"

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_routes.main_routes)
    app.register_blueprint(users_routes.users_routes)
    app.register_blueprint(add_routes.add_routes)
    app.register_blueprint(del_routes.del_routes)
    app.register_blueprint(update_routes.update_routes)
    app.register_blueprint(analytics.analytics)
    # db.create_all()
    return app
