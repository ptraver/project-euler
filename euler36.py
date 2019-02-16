
"""
The decimal number, 585 = 1001001001 base 2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


#converts decimal to binary
def dec_to_bin(x):
    return int(bin(x)[2:])


answer = 0


for i in range(1000000):

	str_dec = str(i)
	str_bin = str(dec_to_bin(i))

	if str_dec[::-1] == str_dec and str_bin[::-1] == str_bin:
		answer += i

print(answer)
