from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import Player  # Update the import to use Player
from app.forms import RegistrationForm, LoginForm

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            if Player.query.filter_by(email=email).first():
                flash('Email already exists!')
                return redirect(url_for('register'))
            new_player = Player(player_name=name, email=email, password=password, created_at=datetime.now())
            db.session.add(new_player)
            db.session.commit()
            flash('Player registered successfully!')
            return redirect(url_for('login'))
        else:
            print("Form validation failed")
            print(form.errors)
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        player = Player.query.filter_by(player_name=name, email=email).first()
        if player:
            login_user(player)
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your name and email.')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('login'))

@app.route('/users')
@login_required
def users():
    all_users = Player.query.all()  # Update to use Player
    return render_template('users.html', users=all_users)
