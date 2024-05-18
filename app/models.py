from app import db
from flask_login import UserMixin

class Player(UserMixin, db.Model):
    __tablename__ = 'Player'
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_name = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<Player {self.player_name}>'
