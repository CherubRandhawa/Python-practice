def anagram():
    if len(s) != len(t):
	    eturn false                                              
    m = {}

    for i in range(0, len(s)):
	    if s[i] in m:
		    m[s[i]] += 1
	    else:
		    m[s[i]] = 1

    for j in range(0, len(t)):
	    if t[j] not in m:
		    return False
	    else:
		    x = t.count(t[j])
		    if x != m[t[j]]:
			    return False
	
    return True