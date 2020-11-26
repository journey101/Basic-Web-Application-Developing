from flask import Flask
from basic_twit_app.routes import main_routes, add_routes, users_routes, get_routes, del_routes
from basic_twit_app.models import db, migrate


DATABASE_URI = "sqlite:///twit.sqlite3"

# factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_routes.main_routes)
    app.register_blueprint(users_routes.users_routes, url_prefix='/users')
    app.register_blueprint(add_routes.add_routes)
    app.register_blueprint(get_routes.get_routes)
    app.register_blueprint(del_routes.del_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)