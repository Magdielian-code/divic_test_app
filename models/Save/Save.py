from frappe import _dict, get_meta

class Save:
    def __init__(self, data):
        meta = get_meta('Save')
        self.doc = _dict(data)
        self.doc.doctype = 'Save'
