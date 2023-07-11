"""Blogly application."""
from flask import Flask, render_template, redirect, flash, request # session
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db 
from forms import AddPet, EditPet

# Create a FLASK instance
app = Flask(__name__)
# Add a DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# SECRET KEY
app.config['SECRET_KEY'] = "hyptokrypo"
# DEBUG TOOLBAR
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# initializes the Flask Debug Toolbar
debug = DebugToolbarExtension(app)
# connect to DATABASE
connect_db(app)

with app.app_context():
	# db.drop_all()
	db.create_all()

@app.route('/')
def home():
	"""Home page with list of all pets"""
	pets = Pet.query.all()
	return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
	"""Add new pet"""
	form = AddPet()
	# form.validate_on_submit == checks if this is a POST request? AND is the TOKEN valid?
	if form.validate_on_submit():
		name = form.name.data
		species = form.species.data
		photo_url = form.photo_url.data
		age = form.age.data
		notes = form.notes.data
		new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
		db.session.add(new_pet)
		db.session.commit()
		return redirect('/')
	else:
		return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=["GET"])
def show_pet(pet_id):
		"""Show pet details"""
		pet = Pet.query.get_or_404(pet_id)
		return render_template('pet.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit deatails about Pet and update in database"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet_id}')
        
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
        
# Run the app
if __name__ == '__main__':
	app.run()
