"""
	Finding the greatest common divisor
"""


# Using recursion
def gcd_recursive(a, b):
	if b == 0:
		return a
	return gcd_recursive(b, a % b)


# Using loops
def gcd_loops(a, b):
	smaller = a
	gcd = 1

	if b > a:
		smaller = b

	for i in range(1,smaller + 1):
		if (a % i == 0) and (b % i == 0):
			gcd = i

	return gcd


# Using the Euclidean algorithm
def gcd_euclidean(a, b):
	while b:
		temp = a
		a = b
		b = temp % b

	return a
