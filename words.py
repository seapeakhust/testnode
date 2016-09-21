with open('test.txt') as f:
    lines = f.readlines()
rowIndex=1
allwords={}
for line in lines:
	words = line.split()
	for word in words:
		if allwords.get(word) == None:
			allwords[word] = []
		allwords[word].append(rowIndex);
	rowIndex += 1
outputwords = sorted(allwords.items(), lambda x,y: cmp(len(x[1]),len(y[1])), reverse=True)
for outputword in outputwords:
	print str(len(outputword[1])) + " " + outputword[0] + " " + str(outputword[1])