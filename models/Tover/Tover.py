from frappe import _dict, get_meta

class Tover:
    def __init__(self, data):
        meta = get_meta('Tover')
        self.doc = _dict(data)
        self.doc.doctype = 'Tover'
