# Copyright (c) 2025, Solomon Lamkhothang and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import re

class Venue(Document):
	def validate(self):
		# Email Validation
		if self.email and not re.match(r"[^@]+@[^@]+\.[^@]+",self.email):
			frappe.throw(_("Invalid email format"))

		# Phone Validation (digits only, has to be 10 digits)
		if self.phone and not re.match(r"^\d{10}$",self.phone):
			frappe.throw(_("Enter Valid phone Number"))
		# Coordinate validation
		if self.coordinates and not re.match(r"^-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?$", self.coordinates):
			frappe.throw(_("Coordinates must be latitude, longitude format"))
