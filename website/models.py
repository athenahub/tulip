from . import db

from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    images = db.relationship('Image')
    likes = db.relationship('Like')
    downloads = db.relationship('Download')

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_path = db.Column(db.String, nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, timezone=True)
    likes = db.relationship('Like')
    downloads = db.relationship('Download')
    image_tags = db.relationship('ImageTag')
    dominant_colors = db.relationship('DcominantColor')

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    like_date = db.Column(db.DateTime, nullable=False, timezone=True)

class Download(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    download_date = db.Column(db.DateTime, nullable=False, timezone=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False, unique=True)
    image_tags = db.relationship('ImageTag')

class ImageTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)

class DominantColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    color_hex = db.Column(db.String(7), nullable=False)
