# -*- encoding: utf-8 -*-
#NWD(liczba całkowita a, liczba całkowita b)
#       dopóki b != 0
#           c := reszta z dzielenia a przez b
#           a := b
#           b := c
#       zwróć a

import sys

def euklides(a, b):
	while b <> 0:
		c = a%b
		a = b
		b = c
	return a

if __name__ == "__main__":
	print euklides(int(sys.argv[1]), int(sys.argv[2]))
