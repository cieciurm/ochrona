#Function exp-by-squaring(x,n)
#     if n=1 then return x;
#		      else if n is even then return exp-by-squaring(x*x, n/2);
#					     else if n is odd then return x * exp-by-squaring(x*x, (n-1)/2).

import sys

def exponent(x, n):
	print "* Podnosze %d do %d" % (x, n)
	if n == 1:
		print "* n == 1"
		return x
	if n%2 == 0:
		print "* n jest parzyste"
		return exponent(x*x, n/2)
	else:
		print "* n jest nieparzyste"
		return x*exponent(x*x, (n-1)/2)

if __name__ == "__main__":
	print "== %d" % exponent(int(sys.argv[1]), int(sys.argv[2]))
