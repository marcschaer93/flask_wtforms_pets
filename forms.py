from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, IntegerRangeField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPet(FlaskForm):
    name = StringField("Pet name", validators=[InputRequired(), Length(min=3, max=20, message="Name must be between 3 and 20 characters")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL")]) 
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("Available?")

class EditPet(FlaskForm):
    notes = StringField("Notes")
    available = BooleanField("Available?")
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL")])
    
