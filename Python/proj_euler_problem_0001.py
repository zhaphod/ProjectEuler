'''
Problem 1
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum = 0

def EulerProblem0001():
	global sum
	for i in range(1, 1000):
		if i % 5 == 0 or i % 3 == 0:
				print(i, end=" ")
				sum += i

	print("Sum with for loop = " + str(sum))
	sum = 0
	sum += 3 * (333 * 334 / 2)
	sum += 5 * (199 * 200 / 2)
	sum -= 15 * (66 * 67 / 2)
	print("Sum with closed form = " + str(sum))
	
if __name__ == "__main__":
	print("Euler problem one")
	EulerProblem0001()
	print("Sum = " + str(sum))
	