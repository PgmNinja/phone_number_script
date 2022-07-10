import base64
import time
import sys

#Import common methods
sys.path.insert(1, '../common/')
from animation import animation

def decode_base64(secret_string):
    base64_bytes = secret_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    return string_bytes.decode("ascii")

def find_phone(string):
	start = time.time()
	decoded_num=string
	while True:
		decoded_num=decode_base64(decoded_num)
		try:
			int(decoded_num)
			break
		except Exception as e:
			continue
	end = time.time()
	animation(end-start)
	return decoded_num

def main():
	string = input('Enter the encrypted string: ')
	sys.stdout.write(str(find_phone(string))+"\n")

if __name__ == '__main__':
	main()
