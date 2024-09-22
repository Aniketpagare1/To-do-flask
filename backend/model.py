from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500))  # Only for Pro users

    def __repr__(self):
        return f"<ToDo {self.title}>"
