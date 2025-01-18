from config import db


class Publisher(db.Model):
    __tablename__ = 'tbl_pub'  # Ensure the table name matches the one in the database
    
    id_pub = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id_pub with auto_increment
    nama_pub = db.Column(db.String(255), nullable=False)  # nama_pub as the publisher's name with varchar(255)

    games = db.relationship('Game', back_populates='publisher_rel')

    def to_dict(self):
        return {
            'id_pub': self.id_pub,
            'nama_pub': self.nama_pub
        }
