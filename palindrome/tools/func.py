# Module func
def is_palindrome(word):
	'''

	'''
	def_res = False
	if (word != '' and len(word) > 1):
		half_array = int(len(word)/2)
		chr_array = list(word.lower())
		begin_array = chr_array[0:half_array]
		begin_array.reverse()
		end_array = chr_array[len(chr_array)-half_array:len(chr_array)]
		if (begin_array == end_array):
			def_res = True
	return def_res

#Test function is_palindrome
if (__name__ == '__main__'):
	print('empty string is {}'.format(is_palindrome('')))
	print('A string is {}'.format(is_palindrome('A')))
	print('abc string is {}'.format(is_palindrome('abc')))
	print('abccba string is {}'.format(is_palindrome('abccba')))
	print('abcncba string is {}'.format(is_palindrome('abcncba')))
	print('Тестовый string is {}'.format(is_palindrome('Тестовый')))
	print('KUULILENNUTEETUNNELILUUK string is {}'.format(is_palindrome('KUULILENNUTEETUNNELILUUK')))
	print('AbCncba string is {}'.format(is_palindrome('AbCncba')))