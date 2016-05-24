#!/usr/bin/env python

class Intertechno:

	state = {
		1: 'FF', 	# ON
		0: 'F0'		# OFF
	}

	systemCode = {
		'A':  '0000',
		'B':  'F000',
		'C':  '0F00',
		'D':  'FF00',
		'E':  '00F0',
		'F':  'F0F0',
		'G':  '0FF0',
		'H':  'FFF0',
		'I':  '000F',
		'J': 'F00F',
	 	'K': '0F0F',
		'L': 'FF0F',
		'M': '00FF',
		'N': 'F0FF',
		'O': '0FFF',
		'P': 'FFFF'
	}

	deviceCode = {
		1:  '0000',
		2:  'F000',
		3:  '0F00',
		4:  'FF00',
		5:  '00F0',
		6:  'F0F0',
		7:  '0FF0',
		8:  'FFF0',
		9:  '000F',
		10: 'F00F',
	 	11: '0F0F',
		12: 'FF0F',
		13: '00FF',
		14: 'F0FF',
		15: '0FFF',
		16: 'FFFF'
	}

	def translate(self, sCode, dCode, targetState):
		try:
			switchState = self.state[1] if targetState == True else self.state[0]
			return self.systemCode[sCode] + self.deviceCode[dCode] + '0F' + switchState
		except KeyError:
			print("invalid code was passed to the function.")
			print("	SystemCode [A-P]")
			print("	DeviceCode 0-16")
			print("	State      0-1")
			print("returning None back to caller.")
			return None