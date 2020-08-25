#leetcode 752. Open the Lock
"""
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
"""
import collections 
def openLock(self, deadends: List[str], target: str) -> int:
    #0000 to 9999 are all nodes in the graph, if the tuning is in (-1,1) between two nodes, there is a edge 
    #need to have a functin to perform the breath first search 
    #finding all neighbours
    def neighbours(node):
        #iterate through all the digits 
        for i in range(4):
            val = node[i]
            #tuning wheels forward or backward 
            for step in (-1,1):
                val_change = (val+step)%10
            yield node[:i] + str(val_change) + node[i+1:]
        
        queue = collections.deque([('0000',0)])
        deads = set(deadends)
        seen = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deads:
                continue
            for nb in neighbours(node):
                if nb not in seen:
                    seen.add(nb)
                    queue.append((nb, depth+1))

        #if there is no shorest path, then -1
        return -1 