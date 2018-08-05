
def is_prime(num):
	if num>1:
		for i in range (2,num):
			if (num%i)==0:
				print("is not a prime number")
				break
		else:
			print("is a prime number")
	else:
		print("is not a prime number")
is_prime(5191)