#!/usr/bin/python3

alpha = "abcdefghijklmnopqrstuvwxyzabcabcdefghijklmnopqrstuvwxyzabc"

draft_string = input("Enter Here -> ")
times_rotate = int(input("Numbers only-> "))

output_string = ""

for i in draft_string:
	if i in alpha:
		output_string += alpha[alpha.index(i) + times_rotate]
	else:
		output_string += i

print(output_string)