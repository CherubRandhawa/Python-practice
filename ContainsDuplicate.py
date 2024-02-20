def containsduplicate():
    m = {}
    for i in range(0, len(lst)):
	    if lst[i] in m:
		    return True
		else:
		    m[lst[i]] = i
    return False