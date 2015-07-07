#open txt file with text where is palindrome words
#with help reg exp define words
#define that words witch are palindrome and write to out file
import re
import os
from tools.func import is_palindrome

APPLICATION = 'more'
IN_FILE_NAME = 'in_text.txt'
OUT_FILE_NAME = 'out_text.txt'

file_in = None
try:
	file_in = open(IN_FILE_NAME,'rt',encoding='utf-8')
	
	reg_expr = r'\W+'
	reg_obj = re.compile(reg_expr)
	
	file_in.seek(0)
	line = file_in.readline()
	file_out = open(OUT_FILE_NAME,'wt',encoding='utf-8')
	while (len(line) > 0):
		#words_list = [word for word in reg_obj.split(line) if is_palindrome(word)]
		for word in reg_obj.split(line):
			if is_palindrome(word):
				file_out.write('{}\n'.format(word))
		line = file_in.readline()
			
	file_out.close()

	os.system(APPLICATION + ' ' + OUT_FILE_NAME)

except IOError as err:
	print(err)
else:
	print('All Done !!!')
finally:
	if (file_in is not None):
		file_out.close()