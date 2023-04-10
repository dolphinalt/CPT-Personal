from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

def findId(username): 
    id = User.query.filter_by(_username=username).first().id
    return id 

def findUser(username): 
    user = User.query.filter_by(_username=username).first()
    return user

def class_obj_by_username(username):
    return User.query.filter_by(username=username).first()


class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            username = body.get('username')
            if username is None or len(username) < 2:
                return {'message': f'Username is missing, or is less than 2 characters'}, 210
            fullname = body.get('fullname')
            if fullname is None or len(fullname) < 2:
                return {'message': f'Fullname is missing, or is less than 2 characters'}, 210
            # validate grade
            grade = body.get('grade')
            if grade is None:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            password = body.get('password')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(username=username, fullname=fullname, password=password,  grade=grade)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                uo.set_password(password)
            # convert to date type
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {username}, either a format error or duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = User.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Authenticate(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            password = body.get('password')
            if len(username) < 1:
                return {'message': f'Invalid username'}, 210
            if len(password) < 1:
                return {'message': f'Empty Password'}, 210

            user = findUser(username)
            id = findId(username)
            if user.is_password(password):
                return username + ":" + str(id)
            return None
    
    class _Schedules (Resource):
        def get(self):
            users = Users.query.all()
            json_ready = [user.read() for user in users]
            return jsonify(json_ready)

    class _UpdateSchedules(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            id = findId(username)
            p1 = body.get('p1')
            p2 = body.get('p2')
            p3 = body.get('p3')
            p4 = body.get('p4')
            p5 = body.get('p5')
            t1 = body.get('t1')
            t2 = body.get('t2')
            t3 = body.get('t3')
            t4 = body.get('t4')
            t5 = body.get('t5')
            user = class_obj_by_username(username)
            print(user)
            if user:
                user.update(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5)
            else:
                return {'message': f"unable to find user '{username}'"}, 210
            return user.read()

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_UpdateSchedules, '/schedules/update')
    api.add_resource(_Schedules, '/schedules')
    api.add_resource(_Authenticate, '/auth')