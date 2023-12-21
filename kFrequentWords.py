#Leetcode 692

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = {} #to count the occurences of words 
        ans = []
        for i in range(0, len(words)): # if words are not in map add them or inc their count
            if words[i] not in map:
                map[words[i]] = 1
            else:
                map[words[i]] += 1
        
        sorted_dict = sorted(map.items(), keys = lambda x:(-x[1], x[0])) #sorting dict in descending order and if values equal in ascending. -x[1] denotes first value and - is descending order

        for i in range(0,k):
            ans.append(sorted_dict[i][0]) #0 to only include key and not values
        return ans  