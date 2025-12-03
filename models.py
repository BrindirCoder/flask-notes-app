from app import db
from datetime import datetime


class NoteData(db.Model):
    __tablename__ = "notedata"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(
        db.String(50),
        default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        nullable=False,
    )

    def __repr__(self):
        return f"<Note {self.title}>"
