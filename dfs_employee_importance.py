#PROBLEM 
#690. Employee Importance
"""
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
"""
employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
d = 1 
def getImportance( employees, id: int) -> int:
    weight_sum = 0 

    def find_child(master, alist, child):
        if master == []:
            return [] 
        else:
            for i in master:
                child.append(alist[i-1][1])
                find_child(alist[i-1][2],alist,child)
            return child 
    all_child = find_child(employees[d-1][2], employees, [])
    weight_sum = sum(all_child)+employees[d-1][1]

    return weight_sum


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
def getImportance(self, employees:List[Employee], id):
    #return of this getImportance will be getting importance for current node 
    #each node has id , value and child 
    #convert into map 
    """not optimal"""
    employee_map = {emp.id:emp for emp in employees}
    result = employee_map[id].importance

    #find child importance 
    for child in employee_map[id].subordinates:
        result += self.getImportance(employees,child)
    return result 

def getImportance1(self, employees:List[Employee], id:int)->int:
    employee_map = {emp.id: emp for emp in employees}
    #map all the employee in a hash map  
    def dfs(employee, map):
        result = employee.importance
        for child in employee.subordinates:
            result += dfs(map[child],map)
        return result 

    return dfs(employee_map[id],employee_map)

