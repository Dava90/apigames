from config import db

class Developer(db.Model):
    __tablename__ = 'tbl_dev'  # Define the table name explicitly (optional but recommended)
    
    id_dev = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_dev = db.Column(db.String(255), nullable=False)

    # Assuming you have a relationship with a Game model (adjust as needed)
    games = db.relationship('Game', back_populates='developer_rel')

    def to_dict(self):
        return {
            'id_dev': self.id_dev,
            'nama_dev': self.nama_dev
        }
