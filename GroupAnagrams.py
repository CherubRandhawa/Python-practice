def sortstr(self, s):
	return "".join(sorted(s))

def groupanagrams():
	m = {}
	arr = []
	for i in range(0, len(strs)):
		hashed = self.sortstr(strs[i])
		if hashed not in m:
			m[hashed] = []
		m[hashed].append(strs[i])
	
	for j in m.values:
		arr.append(j)
	return arr
