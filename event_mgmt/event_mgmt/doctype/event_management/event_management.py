# Copyright (c) 2025, Solomon Lamkhothang and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class EventManagement(Document):
	def validate(self):
		#Date Logic
		if self.end_date and self.start_date and self.end_date < self.start_date:
			frappe.throw(_("End Date must be after Start Date"))
		# Venue Capacity
		if self.venue:
			venue_doc = frappe.get_doc("Venue",self.venue)
			if self.capacity and venue_doc.capacity and self.capacity > venue_doc.capacity:
				frappe.throw(_(f"Event Capacity ({self.capacity}) exceeds Venue Capacity ({venue_doc.capacity})"))
