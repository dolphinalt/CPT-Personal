""" database dependencies to support sqliteDB examples """
import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table

class Classes(db.Model):
    __tablename__ = 'classes'

    # Define the Classes schema
    id = db.Column(db.Integer, primary_key=True)
    # Define a relationship in classes Schema to userID who originates the classes, many-to-one (many classes to one user)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    per1 = db.Column(db.String(255), unique=False, nullable=False)
    per2 = db.Column(db.String(255), unique=False, nullable=False)
    per3 = db.Column(db.String(255), unique=False, nullable=False)
    per4 = db.Column(db.String(255), unique=False, nullable=False)
    per5 = db.Column(db.String(255), unique=False, nullable=False)
    teach1 = db.Column(db.String(255), unique=False, nullable=False)
    teach2 = db.Column(db.String(255), unique=False, nullable=False)
    teach3 = db.Column(db.String(255), unique=False, nullable=False)
    teach4 = db.Column(db.String(255), unique=False, nullable=False)
    teach5 = db.Column(db.String(255), unique=False, nullable=False)
    

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, per1, per2, per3, per4, per5, teach1, teach2, teach3, teach4, teach5):
        self.userID = id
        self.per1 = per1
        self.per2 = per2
        self.per3 = per3
        self.per4 = per4
        self.per5 = per5
        self.teach1 = teach1
        self.teach2 = teach2
        self.teach3 = teach3
        self.teach4 = teach4
        self.teach5 = teach5
        


    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Classes(" + str(self.userID) + "," + self.per1 + "," + self.per2 + "," + self.per3 + "," + self.per4 + "," + self.per5  + "," + self.teach1 + "," + self.teach2 + "," + self.teach3 + "," + self.teach4 + "," + self.teach5  + ","+ str(self.userID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        
        return {
            "userID": self.userID,
            "per1": self.per1,
            "per2": self.per2,
            "per3": self.per3,
            "per4": self.per4,
            "per5": self.per5,
            "teach1": self.teach1,
            "teach2": self.teach2,
            "teach3": self.teach3,
            "teach4": self.teach4,
            "teach5": self.teach5
        }

    def update(self, id="", per1="", per2="", per3="", per4="", per5="", teach1="", teach2="", teach3="", teach4="", teach5=""):
        #only updates values with length
        self.userID = id
        if len(per1) and len(per2) and len(per3) and len(per4) and len(per5) and len(teach1) and len(teach2) and len(teach3) and len(teach4) and len(teach5)> 0:
            self.per1 = per1
            self.per2 = per2
            self.per3 = per3
            self.per4 = per4
            self.per5 = per5
            self.teach1 = teach1
            self.teach2 = teach2
            self.teach3 = teach3
            self.teach4 = teach4
            self.teach5 = teach5
        db.session.commit()
        return self

class User(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    
    
    _username = db.Column(db.Text, unique=True, nullable=False)
    _fullname = db.Column(db.Text, unique=False, nullable=False)
    _password = db.Column(db.Text, unique=False, nullable=False)
    _grade = db.Column(db.Integer, unique=False, nullable=False)
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, username, fullname, password="letmein", grade=9):
        self._username = username    # variables with self prefix become part of the object, 
        self._fullname = fullname
        self.set_password(password)
        self._grade = grade

    # a name getter method, extracts name from object
    @property
    def username(self):
        return self._username
    

    # a setter function, allows name to be updated after initial object creation
    @username.setter
    def username(self, username):
        self._username = username
    
    # a getter method, extracts email from object
    @property
    def fullname(self):
        return self._fullname
    
    # a setter function, allows name to be updated after initial object creation
    @fullname.setter
    def fullname(self, fullname):
        self._fullname = fullname

    def get_id(self):
        return self.id
    
    @property
    def password(self):
        return self._password[0:5] + "..." # because of security only show 1st characters

    # update password, this is conventional setter
    def set_password(self, password):
        #Create a hashed password.
        self._password = generate_password_hash(password, method='sha512')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        #Check against hashed password.
        result = check_password_hash(self._password, password)
        if result:
            return True
        else:
            return False
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def grade(self):
        return self._grade
    
    # a setter function, allows name to be updated after initial object creation
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    
    def read(self):
        return {
            "id": self.id,
            "username": self.username,
            "fullname": self.fullname,
            "grade": self.grade,
            "classes": [period.read() for period in self.classes],
        }

    def update(self, username="", fullname="", password=""):
        #only updates values with length
        if len(username) > 0:
            self.username = username
        if len(fullname) > 0:
            self.fullname = fullname
        if len(password) > 0:
            self.set_password(password)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None



# Builds working data for testing
def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()

        
        u1 = User(username='eris29', id=u1.id, fullname='Alexander Lu', password='CyberPatriot1!', grade=11, per1="AP English Language", per2="AP Calculus BC", per3="AP Physics C: Mechanics", per4="Court Sports", per5="AP Computer Science: Principles", teach1="Cara-Lisa Jenkins", teach2="Michelle Lanzi-Sheaman", teach3="Ifeng Liao", teach4="Dale Hanover", teach5="Sean Yeung")
        u2 = User(username='dolfin', fullname='Ethan Zhao', password='CyberPatriot2@', grade=10)
        u2 = User(username='dolfin', fullname='Ethan Zhao', password='CyberPatriot3#', grade=11)
        u3 = User(username='shattered', fullname='Sophia Tang', password='CyberPatriot3#', grade=10)
        u4 = User(username='calicocat', fullname='Lily Wu', password='CyberPatriot4$', grade=11)

        # Inserting test data into Classes table
        #u1.append(Classes())
        #u2.append(Classes(id=u2.id, per1="AP Calculus AB", per2="AP Biology", per3="Honors Humanities 2", per4="AP Chinese", per5="AP Computer Science: Principles", teach1="Briana West", teach2="Julia Cheskaty", teach3="Jennifer Philyaw", teach4="Ying Tzy Lin", teach5="Sean Yeung"))
        #u3.append(Classes(id=u3.id, per1="AP Chemistry", per2="Intro to Finance", per3="AP World History", per4="AP Calculus AB", per5="AP Computer Science: Principles", teach1="Kenneth Ozuna", teach2="Amanda Nelson", teach3="Megan Volger", teach4="Cherie Nydam", teach5="Sean Yeung"))
        #u4.append(Classes(id=u4.id, per1="AP English Language", per2="AP Computer Science A", per3="AP US History", per4="AP Statistics", per5="AP Computer Science: Principles", teach1="Cara-Lisa Jenkins", teach2="John Mortensen", teach3="Thomas Swanson", teach4="Michelle Derksen", teach5="Sean Yeung"))
        
        users = [u1, u2, u3, u4]
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate uid, or error: {user.uid}")
        
        
    