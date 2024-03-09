from frappe import _dict, get_meta

class Game:
    def __init__(self, data):
        meta = get_meta('Game')
        self.doc = _dict(data)
        self.doc.doctype = 'Game'
