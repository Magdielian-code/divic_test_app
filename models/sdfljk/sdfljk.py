from frappe import _dict, get_meta

class sdfljk:
    def __init__(self, data):
        meta = get_meta('sdfljk')
        self.doc = _dict(data)
        self.doc.doctype = 'sdfljk'
