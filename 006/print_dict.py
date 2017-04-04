#!python3
#print_dict.py is a script to print the contents of a dict

some_dict = {"Julian": 25, "Bob": 26, "Dan": 47, "Cornelius": 3}

def print_dict(dictionary):
	for k, v in dictionary.items():
		print('\n{}: {}'.format(k, v))	

print_dict(some_dict)
