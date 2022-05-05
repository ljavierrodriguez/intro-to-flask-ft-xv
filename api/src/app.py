from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from models import db, Role, User, Profile

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" # sqlite, mysql, oracle, postgresql 

db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/roles', methods=['GET'])
def all_roles():
    roles = Role.query.all() # SELECT * FROM roles; => [<Role>, <Role>, <Role>]
    #print(roles)
    roles = list(map(lambda role: role.serialize(), roles))
    #print(roles)
    return jsonify(roles), 200

@app.route('/api/roles', methods=['POST'])
def add_role():
    name = request.json.get('name')
    if not name: return jsonify({ "msg": "El nombre es requerido!"}), 400

    role = Role()
    role.name = name
    role.save() # db.session.add y db.session.commit

    data = {
        "code": 201,
        "message": "Role created successfully!",
        "status": "ok",
        "role": role.serialize()
    }
    return jsonify(data), 201

@app.route('/api/roles/<int:id>', methods=['PUT'])
def update_role(id):
    name = request.json.get('name')
    if not name: return jsonify({ "msg": "El nombre es requerido!"}), 400

    role = Role.query.get(id)
    if not role: return jsonify({ "msg": "El role no existe!"}), 404

    role_exits = Role.query.filter_by(name=name).first()
    if role_exits and role_exits.id != id: return jsonify({ "msg": 'El role %s ya existe!' % role_exits.name}), 400 

    # f'Hola {name}'
    # 'Hola %s' % name

    role.name = name
    role.update() # db.session.commit

    data = {
        "code": 200,
        "message": "Role updated successfully!",
        "status": "ok",
        "role": role.serialize()
    }
    return jsonify(data), 200


@app.route('/api/register', methods=['POST'])
def register():

    name = request.json.get('name')
    email = request.json.get('email')
    bio = request.json.get('bio', "")
    role = request.json.get("role")

    obj_role = Role.query.filter_by(name=role).first()

    """    
    user = User()
    user.name = name
    user.email = email
    user.save()

    profile = Profile()
    profile.bio = bio
    profile.user_id = user.id
    profile.save() 
    """

    user = User()
    user.name = name
    user.email = email
    user.roles.append(obj_role)
    
    profile = Profile()
    profile.bio = bio
    
    user.profile = profile # asigno ese profile a user
    user.save()

    data = {
        "code": 201,
        "message": "User created successfully!",
        "status": "ok",
        "user": user.serialize()
    }

    return jsonify(data), 201



if __name__ == '__main__':
    app.run()
