class CrazyitDict(dict):
    def key_from_value(self, val):
        for key in self.keys():
            if self[key] == val:
                return key
        return None

    def remove_by_value(self, val):
        for key in self.keys():
            if self[key] == val:
                self.pop(key)
                return None
