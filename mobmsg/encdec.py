"""
	{
		"created_on": "14 June 2017",
		"aim": "To perform encode decode for mobile messaging components",
	}
"""

class MobileMessage():
	""" A class that defines that defines the states & methods for mobile messaging"""
	def __init__(self, mobile_number, customer_id, sms_id):
		self.mobile_number = str(mobile_number)
		self.customer_id = str(customer_id)
		self.sms_id = str(sms_id)
		self.combined_data = self.mobile_number + self.customer_id + self.sms_id
		self.encoded_msg = ""
		self.decoded_msg = ""
		self.encoded_msg_len = 0
		self.decoded_msg_len = 0
		self.encoded = False
		self.decoded = False

	def is_valid(self):
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

	def encode(self):
		""" A method that encodes the message """
		if not self.is_valid():
			return

		start = 0
		for last in range(2, 21, 2):
			self.encoded_msg += chr(int(self.combined_data[start:last]))
			start += 2
		self.encoded_msg_len = len(self.encoded_msg)
		self.encoded = True


	# def decode(self):
	# 	""" A method that encodes the message """
	# 	if not self.is_valid():
	# 		return

	# 	self.decoded = True

	def details(self):
		""" A method that displays the details """
		if not self.encoded:
			print "\nMessage encoding is required to get the details"
			return

		# if !self.decoded:
		# 	print "\nMessage encoding is required to get the details"
		# 	return

		print "========================== ORIGINAL DATA ============================"
		print "Mobile number : ", self.mobile_number
		print "Customer id : ", self.customer_id
		print "SMS id : ", self.sms_id
		print "Combined data : ", self.combined_data
		print "\n========================== ENCODED DATA ============================"
		print "Encoded message        : ", self.encoded_msg
		print "Encoded message length : ", self.encoded_msg_len
		print "\n========================== DECODED DATA ============================"
		print "Encoded message        : ", self.decoded_msg
		print "Encoded message length : ", self.decoded_msg_len

def main():
	msg = MobileMessage("8461933658", "48345", "98765")
	msg.encode()
	msg.details()

if __name__ == "__main__":
	main()
