def parse_sentence(s="we shall fight them on the beaches", n=2):
    pairs=[]
    words = s.split(" ")
    for i,w in enumerate(words[:len(words)-n+1]):
    	pair=words[i:i+n]
    	#print (i)
    	#print (w)
    	#print (pair)
    	#print (pairs)
    	pairs.append(pair)

    return pairs
if __name__=="__main__":
	print (parse_sentence())
	pairs = parse_sentence()
	print (pairs)
    