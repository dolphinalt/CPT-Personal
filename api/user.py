from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.users import User
import base64

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

def findUser(username): 
    user = User.query.filter_by(_username=username).first()
    return user


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
            password = body.get('password')
            if password is None or len(password) < 2:
                return {'message': f'Password is missing, or is less than 2 characters'}, 210
            p1 = body.get('p1')
            if p1 is None or len(p1) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            p2 = body.get('p2')
            if p2 is None or len(p2) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            p3 = body.get('p3')
            if p3 is None or len(p3) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            p4 = body.get('p4')
            if p4 is None or len(p4) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            p5 = body.get('p5')
            if p5 is None or len(p5) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            t1 = body.get('t1')
            if t1 is None or len(t1) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            t2 = body.get('t2')
            if t2 is None or len(t2) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            t3 = body.get('t3')
            if t3 is None or len(t3) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            t4 = body.get('t4')
            if t4 is None or len(t4) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210
            t5 = body.get('t5')
            if t5 is None or len(t5) < 2:
                return {'message': f'Period 1 is missing, or is less than 2 characters'}, 210

            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(username=username, fullname=fullname, password=password, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5)
            
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
            print(user)
            if user.is_password(password):
                pwbytes=password.encode("ascii")
                b64pw_bytes=base64.b64encode(pwbytes)
                unique=str(b64pw_bytes)[3:11]
                return username + ":" + unique
            return None
    
    class _UserUpdate (Resource):
        def post(self):
            body = request.get_json()
            usernameOld = body.get('usernameOld')
            username = body.get('username')
            fullname = body.get('fullname')
            password = body.get('password')
            user = findUser(usernameOld)
            print(user)
            if user:
                user.update(username=username, fullname=fullname, password=password)
                return jsonify(user.read())
            return {'message': f'Processed {username}, either a format error or duplicate'}, 210

    class _ScheduleUpdate(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
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
            user = findUser(username)
            if user:
                user.update(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5)
            else:
                return {'message': f"unable to find user '{username}'"}, 210
            return user.read()
    
    class _Delete (Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            user = findUser(username)
            if user:
                user.delete()
            else:
                return {'message': f"unable to find user '{username}'"}, 210
            return user.read()

    # building RESTapi endpoint
    api.add_resource(_Create, '/create') # checked and working
    api.add_resource(_Read, '/') # checked and working
    api.add_resource(_ScheduleUpdate, '/updateSchedule') # checked and working
    api.add_resource(_UserUpdate, '/userUpdate') # checked and working
    api.add_resource(_Delete, '/delete') # checked and working
    api.add_resource(_Authenticate, '/auth') # checked and working