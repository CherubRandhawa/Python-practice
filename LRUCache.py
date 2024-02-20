class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity #capacity of cache
        self.cache = {} #map key to node

        self.left, self.right = Node(0,0), Node(0, 0) #2 nodes initialized left and right to track lru and mru left is lru and right is mru, that is why when get is done, node is moved to the right side and removed from left side 
        self.left.next, self.right.prev = self.right, self.left #left node is prev of right and right node is next of left

    #remove node from list by rearranginf DLL pointers    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert node at right
    def insert(self, node):
        prev = self.right.prev #because previous node of the rightmost node will become prev of current node
	prev.next = nxt.prev = node  #to handle the edge case where it could be none
        nxt = self.right #because next node of new node to be added will be rightmost node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])   #remove the value of key using the function to add it to right pointer mru
            self.insert(self.cache[key])   #inserted on rightmost side to mru
            return self.cache[key].val     # return the value of key 
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #this step to remove key and then re insert it with updated value on the right as it is used here again 
        self.cache[key] = Node(key, value) #creating node of key value pair and storing it in cache
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove items from list and delete from lru hashmap. remove left most value as lru
            lru = self.left.next #removed the val next to leftmost pointer
            self.remove(lru)
            del self.cache[lru.key] #removing lru key from cache as well 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


########another better and shhort soln using ordered dict #########
########Pretty self explanatory

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.dic.move_to_end(key)
        else:
            if len(self.dic) < self.cap:
                self.dic[key] = value
            else:
                self.dic.popitem(last=False)
                self.dic[key] = value