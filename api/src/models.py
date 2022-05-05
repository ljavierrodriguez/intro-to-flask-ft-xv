from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# 1 - 1
# 1 - m
# m - n

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('User', secondary="roles_users") # m - n

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def serialize_with_users(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    #role_id = db.Column(db.Integer, nullable=False, db.ForeignKey('roles.id'))
    roles = db.relationship('Role', secondary="roles_users") # m - n
    profile = db.relationship('Profile', backref="user", uselist=False)
    posts = db.relationship('Post', backref="user", lazy=True) # 1 - m
    comments = db.relationship('Comment', backref="user") # 1 - m

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "profile": self.profile.serialize(),
            "roles": self.get_roles()
        }

    def serialize_with_profile(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    def get_roles(self):
        return list(map(lambda role: role.serialize(), self.roles))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200), default="")
    facebook = db.Column(db.String(200), default="")
    twitter = db.Column(db.String(200), default="")
    instagram = db.Column(db.String(200), default="")
    linkedin = db.Column(db.String(200), default="")
    photo = db.Column(db.String(200), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    slug = db.Column(db.String(200), unique=True)
    summary = db.Column(db.String(200))
    body = db.Column(db.Text())
    image = db.Column(db.String(200), default="no-image.png")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment', backref="post") # 1 - m
    # user = db.relationship('User', backref="post", lazy=True)
    


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    #comments = db.relationship('Comment', backref="comments") # 1 - m
    

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    user = db.relationship('User')
    post = db.relationship('Post')