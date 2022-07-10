import base64
import time
import sys

#Import common methods
sys.path.insert(1, '../common/')
from animation import animation

def encode_base64(scret_string):
    string_bytes = scret_string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    return base64_bytes.decode("ascii")

def encode_phone(num, string):
    start = time.time()
    encoded_num = string
    for i in range(int(num)):
        encoded_num = encode_base64(encoded_num)
    end = time.time()
    animation(end-start, 'Encoding...')
    return encoded_num

def main():
    string = input('Enter the phone number: ')
    num = input('Enter how many time you wish to perform encoding: ')
    sys.stdout.write(str(encode_phone(num, string))+"\n")

if __name__ == '__main__':
	main()

