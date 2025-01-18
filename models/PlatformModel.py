from config import db

class Platform(db.Model):
    __tablename__ = 'tbl_plat'  # Menyebutkan nama tabel yang sesuai di database
    id_plat = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id_plat dengan autoincrement
    nama_plat = db.Column(db.String(255), nullable=False)  # nama_plat sesuai dengan kolom pada tabel

    # Jika ada relasi ke tabel lain, Anda dapat mendefinisikannya di sini
    # Misalnya jika Platform memiliki relasi ke tabel Game, maka Anda bisa menambahkannya seperti ini:
    games = db.relationship('Game', back_populates='platform_rel')

    def to_dict(self):
        return {
            'id_plat': self.id_plat,
            'nama_plat': self.nama_plat
        }
