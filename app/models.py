


# class User(UserMixin,db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())


#     password_hash = db.Column(db.String(255))
#     photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
#     reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

#     @property
#     def password(self):
#         raise AttributeError('You cannnot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)


#     def verify_password(self,password):
#         return check_password_hash(self.password_hash,password)


#     def save_user(self):
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f'User {self.username}'
    
    
# class Pitch(db.Model):
#     __tablename__ = 'pitches'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title= db.Column(db.String(300), index=True)
#     content = db.Column(db.String(300), index=True)
#     category_id = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
 
    