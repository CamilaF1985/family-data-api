import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

# Miembros iniciales de la familia
john = {
    "first_name": "John",
    "last_name": "Jackson",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

jane = {
    "first_name": "Jane",
    "last_name": "Jackson",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

jimmy = {
    "first_name": "Jimmy",
    "last_name": "Jackson",
    "age": 5,
    "lucky_numbers": [1]
}

# Añadir miembros a la estructura de datos
jackson_family.add_member(john)
jackson_family.add_member(jane)
jackson_family.add_member(jimmy)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Obtener un miembro específico por id
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is not None:
        # Cambiar "name" por "first_name", y agregar "id", "age", "lucky_numbers"
        return jsonify({
            "id": member.get("id"),
            "first_name": member.get("first_name"),
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers", [])  # Asegúrate de que lucky_numbers exista
        }), 200
    else:
        # Devolver un objeto JSON con el código de estado 404 y un mensaje de error
        return jsonify({"error": "Member not found", "message": "Member not found"}), 404

# Añadir un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    try:
        new_member = request.get_json()
        jackson_family.add_member(new_member)
        return jsonify({}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Eliminar un miembro por id
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        deleted = jackson_family.delete_member(member_id)
        if deleted:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"error": "Member not found", "message": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)



