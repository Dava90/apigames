from config import db

class Genre(db.Model):
    __tablename__ = 'tbl_genre'  # Tentukan nama tabel untuk memastikan sesuai dengan nama tabel di database
    
    id_genre = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Menambahkan autoincrement
    nama_genre = db.Column(db.String(255), nullable=False)  # Menyesuaikan dengan panjang kolom di tabel SQL
    
    games = db.relationship('Game', back_populates='genre_rel')

    def to_dict(self):
        return {
            'id_genre': self.id_genre,
            'nama_genre': self.nama_genre
        }
