import sys #for sys.maxsize to work
from collections import defaultdict

def minTrioDeg(n: int, edges: [int]):
    graph = defaultdict(set) #making a dict set of values to make a graph and nodes
    degree = defaultdict(int) #making one int dict to store degrees as well

    for u,v in edges: #making graphs
        graph[min(u,v)].add(max(u,v))
        degree[u] += 1
        degree[v] += 1
    
    ans = sys.maxsize #This is for ans to have the largest value, could also be inf

    for n1 in range(1, n+1): #this is to traverse fron 1 to the last number in graph that would be 1+n
        for n2 in graph[n1]:
            for n3 in graph[n1]:
                if n3 in graph[n2]:
                    ans = min(ans, degree[n1] + degree[n2] + degree[n3] - 6 ) # 6 subtracted bcoz it formas a trio so 2*3 edges = 6 deg by default 
    return ans if ans<sys.maxsize else -1


