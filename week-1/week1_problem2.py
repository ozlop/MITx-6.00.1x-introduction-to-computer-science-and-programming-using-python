s = 'azcbobobegghakl'
count = 0
matched = 0
target = 'bob'


for check in s:
	string = s[count:count+3]
	if string == target:
		matched +=1
	count += 1

print("Number of times bob occurs is: " + str(matched))
