#!/usr/bin/env python

from intertechno import Intertechno

def main():
	codeBuilder = Intertechno()
	
	print(codeBuilder.translate('A', 1, False))

if __name__ == "__main__":
    main()