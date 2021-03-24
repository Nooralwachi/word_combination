def combination(word):
	result, extra=[], []
	# new_word = word.lower()
	for letter in word:
		if result ==[]:
			result.append(letter.lower())
			result.append(letter.upper())
			#letter.swapcase()
 			# result = [letter, letter.swapcase()]
		else:		
			l = len(result)		
			for i in range(l):	
				pre = result[i]			
				result[i]= pre + letter.lower()
				result.append(pre+letter.upper())	

	print(result)

combination('abc')