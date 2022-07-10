import time
import sys

def animation(runtime, string):
	print(string)
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", \
		"[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

	for i in range(len(animation)):
		time.sleep(runtime)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()

	print("\n")