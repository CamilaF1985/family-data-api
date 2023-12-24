from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        # Inicializar una estructura de familia con un apellido dado
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        # Generar un ID aleatorio para un miembro de la familia
        return randint(0, 99999999)

    def add_member(self, member):
        # Añadir un nuevo miembro a la familia con un ID generado y devolver ese ID
        member_id = self._generateId()
        member["_id"] = member_id
        self._members.append(member)
        return member_id

    def delete_member(self, member_id):
        # Eliminar un miembro de la familia por su ID y devolver True si se realizó la eliminación
        self._members
        initial_length = len(self._members)
        self._members = [m for m in self._members if m.get("id") != member_id]
        return len(self._members) < initial_length

    def get_member(self, member_id):
        # Obtener un miembro de la familia por su ID
        member = next((m for m in self._members if m.get("id") == member_id), None)
        return member

    def update_member(self, member_id, updated_member):
        # Actualizar la información de un miembro existente en la familia
        for i, member in enumerate(self._members):
            if member["_id"] == member_id:
                self._members[i] = updated_member
                self._members[i]["_id"] = member_id
                return True  
        return False  

    def get_all_members(self):
        # Obtener una lista de todos los miembros de la familia
        return self._members





