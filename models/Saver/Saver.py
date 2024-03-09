from frappe import _dict, get_meta

class Saver:
    def __init__(self, data):
        meta = get_meta('Saver')
        self.doc = _dict(data)
        self.doc.doctype = 'Saver'
