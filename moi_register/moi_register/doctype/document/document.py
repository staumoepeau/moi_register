# -*- coding: utf-8 -*-
# Copyright (c) 2020, Dennis Tatila and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Document(Document):
    def on_submit(self):
        self.check_ref()    

    def check_ref(self):
        if not self.ref:
            self.ref = self.get_name()

    def get_name(self):
        return self.name
