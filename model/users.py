""" database dependencies to support sqliteDB examples """
import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table

class User(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    
    
    _username = db.Column(db.Text, unique=True, nullable=False)
    _fullname = db.Column(db.Text, unique=False, nullable=False)
    _password = db.Column(db.Text, unique=False, nullable=False)
    _p1 = db.Column(db.Text, unique=False, nullable=False)
    _t1 = db.Column(db.Text, unique=False, nullable=False)
    _p2 = db.Column(db.Text, unique=False, nullable=False)
    _t2 = db.Column(db.Text, unique=False, nullable=False)
    _p3 = db.Column(db.Text, unique=False, nullable=False)
    _t3 = db.Column(db.Text, unique=False, nullable=False)
    _p4 = db.Column(db.Text, unique=False, nullable=False)
    _t4 = db.Column(db.Text, unique=False, nullable=False)
    _p5 = db.Column(db.Text, unique=False, nullable=False)
    _t5 = db.Column(db.Text, unique=False, nullable=False)
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, username, fullname, password="Password1!", p1=None, p2=None, p3=None, p4=None, p5=None, t1=None, t2=None, t3=None, t4=None, t5=None):
        self._username = username    # variables with self prefix become part of the object, 
        self._fullname = fullname
        self.set_password(password)
        self._p1 = p1
        self._t1 = t1
        self._p2 = p2
        self._t2 = t2
        self._p3 = p3
        self._t3 = t3
        self._p4 = p4
        self._t4 = t4
        self._p5 = p5
        self._t5 = t5

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def fullname(self):
        return self._fullname
    @fullname.setter
    def fullname(self, fullname):
        self._fullname = fullname

    @property
    def password(self):
        return self._password[0:5] + "..." # because of security only show 1st characters
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
    
    @property
    def p1(self):
        return self._p1
    @p1.setter
    def p1(self, p1):
        self._p1 = p1
    @property
    def t1(self):
        return self._t1
    @t1.setter
    def t1(self, t1):
        self._t1 = t1
    
    @property
    def p2(self):
        return self._p2
    @p2.setter
    def p2(self, p2):
        self._p2 = p2
    @property
    def t2(self):
        return self._t2
    @t2.setter
    def t2(self, t2):
        self._t2 = t2
    
    @property
    def p3(self):
        return self._p3
    @p3.setter
    def p3(self, p3):
        self._p3 = p3
    @property
    def t3(self):
        return self._t3
    @t3.setter
    def t3(self, t3):
        self._t3 = t3
    
    @property
    def p4(self):
        return self._p4
    @p4.setter
    def p4(self, p4):
        self._p4 = p4
    @property
    def t4(self):
        return self._t4
    @t4.setter
    def t4(self, t4):
        self._t4 = t4
    
    @property
    def p5(self):
        return self._p5
    @p5.setter
    def p5(self, p5):
        self._p5 = p5
    @property
    def t5(self):
        return self._t5
    @t5.setter
    def t5(self, t5):
        self._t5 = t5
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self, username="", fullname="", password="", p1="", p2="", p3="", p4="", p5="", t1="", t2="", t3="", t4="", t5=""):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            print("User create")
            return self
        except IntegrityError as e:
            db.session.remove()
            print("User create failed")
            print(e)
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    
    def read(self):
        classes = [self.p1 + ";" + self.t1, self.p2 + ";" + self.t2, self.p3 + ";" + self.t3, self.p4 + ";" + self.t4, self.p5 + ";" + self.t5]
        return {
            "username": self.username,
            "fullname": self.fullname,
            "classes": classes
        }

    def update(self, username="", fullname="", password="", p1="", p2="", p3="", p4="", p5="", t1="", t2="", t3="", t4="", t5=""):
        #only updates values with length
        if len(username) > 0:
            self.username = username
        if len(fullname) > 0:
            self.fullname = fullname
        if len(password) > 0:
            self.set_password(password)
        if len(p1) > 0:
            self.p1 = p1
        if len(t1) > 0:
            self.t1 = t1
        if len(p2) > 0:
            self.p2 = p2
        if len(t2) > 0:
            self.t2 = t2
        if len(p3) > 0:
            self.p3 = p3
        if len(t3) > 0:
            self.t3 = t3
        if len(p4) > 0:
            self.p4 = p4
        if len(t4) > 0:
            self.t4 = t4
        if len(p5) > 0:
            self.p5 = p5
        if len(t5) > 0:
            self.t5 = t5
        if len(p6) > 0:
            self.p6 = p6
        if len(t6) > 0:
            self.t6 = t6
        
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()

        
        u1 = User(username='eris29', fullname='Alexander Lu', password='CyberPatriot1!', p1="AP English Language", p2="AP Calculus BC", p3="AP Physics C: Mechanics", p4="Court Sports", p5="AP Computer Science: Principles", t1="Cara-Lisa Jenkins", t2="Michelle Lanzi-Sheaman", t3="Ifeng Liao", t4="Dale Hanover", t5="Sean Yeung")
        u2 = User(username='dolfin', fullname='Ethan Zhao', password='CyberPatriot2@', p1="AP Calculus AB", p2="AP Biology", p3="Honors Humanities 2", p4="AP Chinese", p5="AP Computer Science: Principles", t1="Briana West", t2="Julia Cheskaty", t3="Jennifer Philyaw", t4="Ying Tzy Lin", t5="Sean Yeung")
        u3 = User(username='shattered', fullname='Sophia Tang', password='CyberPatriot3#', p1="AP Chemistry", p2="Intro to Finance", p3="AP World History", p4="AP Calculus AB", p5="AP Computer Science: Principles", t1="Kenneth Ozuna", t2="Amanda Nelson", t3="Megan Volger", t4="Cherie Nydam", t5="Sean Yeung")
        u4 = User(username='calicocat', fullname='Lily Wu', password='CyberPatriot4$', p1="AP English Language", p2="AP Computer Science A", p3="AP US History", p4="AP Statistics", p5="AP Computer Science: Principles", t1="Cara-Lisa Jenkins", t2="John Mortensen", t3="Thomas Swanson", t4="Michelle Derksen", t5="Sean Yeung")

        users = [u1, u2, u3, u4]
        for user in users:
            try:
                user.create()
                print(f"Created user: {user.username}")
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate username, or error: {user.username}")
