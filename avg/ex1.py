#my first programm on python
from random import randint

#declare global and const objects
pattern = '{0:20}	{1:5d}	{2:5d}	{3:5d}\n'
START_RANGE = 0
END_RANGE = 10000

#read towns file and generate random x,y,z 
f_t = open('towns.txt','r')
f_t.seek(0)
out_data = ''
for line in f_t:
	out_data += pattern.format(line.rstrip('\n'), 
								randint(START_RANGE,END_RANGE),
								randint(START_RANGE,END_RANGE),
								randint(START_RANGE,END_RANGE))
f_t.close()

#save out_data
f_in_out = open('in_out.txt','w')
f_in_out.seek(0)
f_in_out.write(out_data)
f_in_out.close()

# read in_out file again and count avg for x,y,z
# and append to file
f_in_out = open('in_out.txt','r+')
f_in_out.seek(0)
x = [] ; y = [] ; z = []
for line in f_in_out:
	row = line.split()
	x.append(int(row[1]))
	y.append(int(row[2]))
	z.append(int(row[3]))
f_in_out.write('=' * 45 + '\n')
f_in_out.write(pattern.format('Avg: ',int(sum(x)/len(x)), int(sum(y)/len(y)), int(sum(z)/len(z))))
f_in_out.close()

#Test console out
#print('Avg x = : {0}, avg y = {1}, avg z = {2}'.format(int(sum(x)/len(x)), int(sum(y)/len(y)), int(sum(z)/len(z))))