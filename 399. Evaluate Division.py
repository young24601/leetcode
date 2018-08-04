# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
#Given some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
#where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
# 
# According to the example above:
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    d = {}
    e = {}
    for i in range(0, len(equations)):
        d[(equations[i][0],equations[i][0])] = 1.0
        d[(equations[i][1],equations[i][1])] = 1.0      
        d[(equations[i][0],equations[i][1])] = values[i]
        d[(equations[i][1],equations[i][0])] = 1.0 / values[i]
        print("d:",d)
        for e1,e2 in d.items():
            print("checking", e1[0], "/", e1[1], "with", equations[i][0], "/", equations[i][1])
            if e1[1] == equations[i][0]:
                print("adding", e1[0], "/", equations[i][1])
                e[(e1[0], equations[i][1])] = values[i] * e2
            if e1[1] == equations[i][1]:
                print("adding", e1[0], "/", equations[i][0])
                e[(e1[0], equations[i][0])] = e2 * 1.0 / values[i]
                
    allEquations = {**d, **e}
    returnValues = []
    for items in queries:
        if tuple(items) in allEquations:
            returnValues.append(allEquations[tuple(items)])
        else:
            returnValues.append(-1.0)

    return returnValues
    
            
# equations = [ ["a", "b"], ["b", "c"] ]
# values = [2.0, 3.0]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

            
# equations = [["a","e"],["b","e"]]
# values = [4.0,3.0]
# queries = [["a","b"],["e","e"],["x","x"]]


equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]


print(calcEquation(equations, values, queries))