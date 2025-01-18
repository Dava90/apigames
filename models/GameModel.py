from config import db
from models.PublisherModel import Publisher
from models.PlatformModel import Platform
from models.GenreModel import Genre
from models.DeveloperModel import Developer
from models.RatingModel import Rating

class Game(db.Model):
    __tablename__ = 'tbl_game'

    # Kolom sesuai dengan tabel
    id_game = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    platform = db.Column(db.Integer, db.ForeignKey('tbl_plat.id_plat'), nullable=False)
    released = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.Integer, db.ForeignKey('tbl_genre.id_genre'), nullable=False)
    developer = db.Column(db.Integer, db.ForeignKey('tbl_dev.id_dev'), nullable=False)
    publisher = db.Column(db.Integer, db.ForeignKey('tbl_pub.id_pub'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, db.ForeignKey('tbl_rating.id_rate'), nullable=False)

    # Relationships
    genre_rel = db.relationship('Genre', back_populates='games')
    developer_rel = db.relationship('Developer', back_populates='games')
    publisher_rel = db.relationship('Publisher', back_populates='games')
    platform_rel = db.relationship('Platform', back_populates='games')
    rating_rel = db.relationship('Rating', back_populates='games')

    def to_dict(self):
        return {
            'id_game': self.id_game,
            'name': self.name,
            'released': self.released,
            'genre': self.genre_rel.nama_genre if self.genre_rel else None,
            'developer': self.developer_rel.nama_dev if self.developer_rel else None,
            'publisher': self.publisher_rel.nama_pub if self.publisher_rel else None,
            'score': self.score,
            'rating': self.rating_rel.nama_rate if self.rating_rel else None,
            'platforms': self.platform_rel.nama_plat if self.platform_rel else None
        }