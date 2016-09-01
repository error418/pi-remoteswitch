#!/usr/bin/env python

from intertechno import Intertechno

def main():
	codeBuilder = Intertechno()
	
	# example: generate code for switching device with code A1 off
	print(codeBuilder.translate('A', 1, False))

if __name__ == "__main__":
    main()
