from frappe import _dict, get_meta

class User:
    def __init__(self, data):
        meta = get_meta('User')
        self.doc = _dict(data)
        self.doc.doctype = 'User'
