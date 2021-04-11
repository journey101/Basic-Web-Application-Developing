from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from basic_twit_app.API.twitter_api import twitter_api


db = SQLAlchemy()
migrate = Migrate()

class Users(db.Model):
    db = SQLAlchemy()

    __tablename__="Users"
    id = db.Column(db.BigInteger, primary_key=True) 
    username = db.Column(db.String)
    full_name = db.Column(db.String)
    followers = db.Column(db.Integer)

    def __repr__(self):
        return "< User {} {} >".format(self.id, self.username)


class Tweet(db.Model):
    db = SQLAlchemy()
    __tablename__ = "Tweet"
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String(1000000))
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.BigInteger, db.ForeignKey("Users.id"))
    user=db.relationship("Users", foreign_keys=user_id)

    def __repr__(self):
        return "< Tweet {} >".format(self.id)

def parse_records(db_records):
    parsed_list = []
    for record in db_records:
        parsed_record = record.__dict__
        print(parsed_record)
        del parsed_record["_sa_instance_state"]
        parsed_list.append(parsed_record)
    return parsed_list