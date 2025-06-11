#!/usr/bin/python3

import string

"""
Generate passwords like 000A to 999Z
password_list = [f"{str(i).zfill(3)}{letter}" for i in range(1000) for letter in string.ascii_uppercase]
"""

# Generate passwords like 0000 to 9999
password_list = [str(i).zfill(4) for i in range(10000)]

# Write each password on a new line
with open("passwords_v2.txt", "w") as file:
	for password in password_list:
		file.write(f"{password}\n")