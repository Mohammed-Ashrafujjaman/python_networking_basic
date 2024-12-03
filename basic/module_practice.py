#!/usr/bin/python3

# In this file we will import the module file to understand how import works in python.

import convertion


# writing a program to convert metrics
def main():
	cm = 200123;
	meter = convertion.convert_CM_to_Meter(cm)
	print(f"{meter} meters")
	meters = 234
	print(f"{convertion.convert_Meter_to_CM(meters)} cm")


if __name__ == '__main__':
	main()