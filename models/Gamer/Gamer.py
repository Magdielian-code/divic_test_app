from frappe import _dict, get_meta

class Gamer:
    def __init__(self, data):
        meta = get_meta('Gamer')
        self.doc = _dict(data)
        self.doc.doctype = 'Gamer'
