# Module to encrypt text
from json import load
from cryptography.fernet import Fernet

'''
def write_key():
	key = Fernet.generate_key()
	with open('key.key', 'wb') as key_file:
		key_file.write(key)
	
write_key()
'''

def load_key():
	file = open('key.key', 'rb')
	key = file.read()
	file.close()
	return key

key = load_key()
fer = Fernet(key)

def view():
	with open('passwords.txt', 'r') as file:
		# Read existing file (loop through lines)
		for line in file.readlines():
			data = line.rstrip()
			user, pwd = data.split('|')
			print(f'User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}')

def add():
	name = input('Username: ')
	pwd = input('Password: ')
	with open('passwords.txt', 'a') as file:
		# Format of added credentials (new line added)
		file.write(f'{name}|{fer.encrypt(pwd.encode()).decode()}\n')

while True:
	mode = input('Would you like to add or view passwords? (view / add) : Press Q to Quit. ').lower()
	if mode == "q":
		break
	elif mode == 'view':
		view()
	elif mode == 'add':
		add()
	else:
		print('Invalid mode')
		continue