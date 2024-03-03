from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from models.database import User
from app import app, socketio,db, login_manager
from app.models.database import User

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    print("reached here")
    print(request.method)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        new_user = User.create_user(username=username, password=password)
        return "holy moly you are registered!!"
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("in this")
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and password==user.password:
            login_user(user)
            # return "HI {}".format(user.username.upper()) 
            print("done")
            return render_template('chatscreen.html')
        else:
            return "Invalid Credentials. Please check creds again"

    return render_template('login.html')

@app.route("/chat")
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    app.logger.info("{} has joined the room {}")
    if username and room:
        return render_template('chat.html',username=username,room=room)
    else:
        return redirect(url_for('home'))

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'],data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement',data)

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} was sent by {} in room {}".format(data['message'], data['username'],data['room']))
    socketio.emit('receive_message',data, room=data['room'])

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))