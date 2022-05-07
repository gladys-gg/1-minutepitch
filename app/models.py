from . import db



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password = db.Column(db.String(255))


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
    
    
# class Pitch(db.Model):
#     __tablename__ = 'pitches'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title= db.Column(db.String(300), index=True)
#     content = db.Column(db.String(300), index=True)
#     category_id = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
 
    