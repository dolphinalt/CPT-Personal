from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.users import User
from model.users import Classes as Schedules

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
    """finds User in table matching username """
    id = User.query.filter_by(_username=username).first().id
    return Schedules.query.filter_by(id=id).first()


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
            users = Schedules.query.all()
            json_ready = [user.read() for user in users]
            return jsonify(json_ready)

    class _UpdateSchedules(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            id = findId(username)
            per1 = body.get('per1')
            per2 = body.get('per2')
            per3 = body.get('per3')
            per4 = body.get('per4')
            per5 = body.get('per5')
            teach1 = body.get('teach1')
            teach2 = body.get('teach2')
            teach3 = body.get('teach3')
            teach4 = body.get('teach4')
            teach5 = body.get('teach5')
            user = class_obj_by_username(username)
            print(user)
            print(id)
            if user:
                user.update(id=id, per1=per1, per2=per2, per3=per3, per4=per4, per5=per5, teach1=teach1, teach2=teach2, teach3=teach3, teach4=teach4, teach5=teach5)
            else:
                return {'message': f"unable to find user '{username}'"}, 210
            return user.read()

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_UpdateSchedules, '/schedules/update')
    api.add_resource(_Schedules, '/schedules')
    api.add_resource(_Authenticate, '/auth')