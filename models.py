"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Initialize the database
db = SQLAlchemy()


def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)

DEFAULT_PET_IMAGE = "https://i0.wp.com/www.animalfoodag.ch/wp-content/uploads/woocommerce-placeholder.png?fit=1200%2C1200&ssl=1"


# MODELS GO HERE
class Pet(db.Model):
	"""Pet Model"""
	__tablename__ = "pets"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.Text, nullable=False)
	species = db.Column(db.Text, nullable=False)	
	photo_url = db.Column(db.Text, nullable=False, default=DEFAULT_PET_IMAGE)	
	age = db.Column(db.Integer, nullable=True)
	notes = db.Column(db.Text, nullable=True)
	available = db.Column(db.Boolean, nullable=False, default=True)



