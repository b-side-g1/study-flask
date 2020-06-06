from models import db,ma
from sqlalchemy import func



class Board(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    writer = db.Column(db.String(20),unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __init__(self, id, writer = None, content = None):
        self.id = id
        self.writer = writer
        self.content = content

class BoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Board
        load_instance = True