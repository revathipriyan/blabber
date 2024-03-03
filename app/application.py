from app import app, socketio

if __name__ =='__main__':
    socketio.run(app,debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# from flask_socketio import SocketIO, join_room
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from sqlalchemy import create_engine
# from sqlalchemy.exc import OperationalError
# from config import Config
# from flask_socketio import SocketIO, join_room

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  
# app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
# db = SQLAlchemy(app)
# socketio = SocketIO(app)

# try:
#     engine = create_engine(Config.DATABASE_URL)
#     connection = engine.connect()
#     print("Database connection successful")
# except OperationalError as e:
#     print("Database connection failed:", e)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# @app.route("/chat")
# def chat():
#     username = request.args.get('username')
#     room = request.args.get('room')
#     app.logger.info("{} has joined the room {}")
#     if username and room:
#         return render_template('chat.html',username=username,room=room)
#     else:
#         return redirect(url_for('home'))

# @socketio.on('join_room')
# def handle_join_room_event(data):
#     app.logger.info("{} has joined the room {}".format(data['username'],data['room']))
#     join_room(data['room'])
#     socketio.emit('join_room_announcement',data)

# @socketio.on('send_message')
# def handle_send_message_event(data):
#     app.logger.info("{} was sent by {} in room {}".format(data['message'], data['username'],data['room']))
#     socketio.emit('receive_message',data, room=data['room'])


