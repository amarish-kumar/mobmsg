"""
	{
		"created_on": "14 June 2017",
		"aim": "To perform encode decode for mobile messaging components",
	}
"""

class MobileMessage():
	""" A class that defines that defines the states & methods for mobile messaging"""
	def __init__(self, mobile_number, customer_id, sms_id):
		self.mobile_number = mobile_number
		self.customer_id = customer_id
		self.sms_id = sms_id
		self.encoded_msg = ""
		self.decoded_msg = ""
		self.encoded_msg_len = 0
		self.decoded_msg_len = 0
		self.encoded = False
		self.decoded = False

	def is_valid():
		""" To check for the exact format like 73537877040123476543 i.e 20 digits """
		import re
		if re.match("^([1-9]{1})([0-9]{9})$", self.mobile_number):
			if(re.match("^[0-9]{5}$", self.customer_id)):
				if re.match("^[0-9]{5}$", self.sms_id):
					return True
				else:
					print "\nInvalid sms id, expected 5 digits got %s"%(self.sms_id)
					return False
			else:
				print "\nInvalid customer id, expected 5 digits got %s"%(self.customer_id)
				return False
		else:
			print "\nInvalid mobile number, expected 10 digits got %s"%(self.mobile_number)
			return False




