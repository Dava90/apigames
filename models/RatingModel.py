from config import db

class Rating(db.Model):
    __tablename__ = 'tbl_rating'  # Specify the table name

    id_rate = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Define the id_rate column with auto-increment
    nama_rate = db.Column(db.String(255), nullable=False)  # Define the nama_rate column

    games = db.relationship('Game', back_populates='rating_rel')

    def to_dict(self):
        return {
            'id_rate': self.id_rate,
            'nama_rate': self.nama_rate
        }
