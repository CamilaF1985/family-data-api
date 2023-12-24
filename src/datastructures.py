from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_id = self._generateId()
        member["_id"] = member_id
        self._members.append(member)
        return member_id

    def delete_member(self, member_id):
        for i, member in enumerate(self._members):
            if member["_id"] == member_id:
                del self._members[i]
                return True  # Indicate success
        return False  # Indicate failure (member not found)

    def get_member(self, member_id):
        member = next((m for m in self._members if m.get("id") == member_id), None)
        return member

    def update_member(self, member_id, updated_member):
        for i, member in enumerate(self._members):
            if member["_id"] == member_id:
                self._members[i] = updated_member
                self._members[i]["_id"] = member_id
                return True  # Indicate success
        return False  # Indicate failure (member not found)

    def get_all_members(self):
        return self._members




