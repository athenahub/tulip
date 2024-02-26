from . import db

from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(150), nullable=False)
    Email = db.Column(db.String(150), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    #images = db.relationship('Image')
    #likes = db.relationship('Like')
    #downloads = db.relationship('Download')

class Image(db.Model):
    __tablename__ = 'Images'
    ImageID = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ImagePath = db.Column(db.String, nullable=False)
    UploadDate = db.Column(db.DateTime(timezone=True), nullable=False)
    #likes = db.relationship('Like')
    #downloads = db.relationship('Download')
    #image_tags = db.relationship('ImageTag')
    #dominant_colors = db.relationship('DominantColor')

class Like(db.Model):
    __tablename__ = 'Likes'
    LikeID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ImageID = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    LikeDate = db.Column(db.DateTime(timezone=True), nullable=False)

class Download(db.Model):
    __tablename__ = 'Downloads'
    DownloadID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ImageID = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    DownloadDate = db.Column(db.DateTime(timezone=True), nullable=False)

class Tag(db.Model):
    __tablename__ = 'Tags'
    TagID = db.Column(db.Integer, primary_key=True)
    TagName = db.Column(db.String(50), nullable=False, unique=True)
    #image_tags = db.relationship('ImageTag')

class ImageTag(db.Model):
    __tablename__ = 'ImageTags'
    ImageTagID = db.Column(db.Integer, primary_key=True)
    ImageID = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    TagID = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)

class Color(db.Model):
    __tablename__ = 'Colors'
    ColorID = db.Column(db.Integer, primary_key=True)
    ImageID = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    ColorHex = db.Column(db.String(7), nullable=False)
