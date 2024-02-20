def isPalindrome(self, s: str) -> bool:
        patterns = [':', ',', '.', '-', '@', '_', "'", '"', '[', ']', '{', '}', '#', '?', ';', '!', '(', ')', '`']
        if len(s) == 1:
            return True
        modstr = s.lower()
        for pattern in patterns:
            if pattern in modstr:
                modstr = modstr.replace(pattern,' ')
        modstr = "".join(modstr.split(' '))
        
        print (modstr)
        if (modstr[0:len(modstr)] == modstr[::-1]):
            return True