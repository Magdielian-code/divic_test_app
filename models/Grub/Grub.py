from frappe import _dict, get_meta

class Grub:
    def __init__(self, data):
        meta = get_meta('Grub')
        self.doc = _dict(data)
        self.doc.doctype = 'Grub'
