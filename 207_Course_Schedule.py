'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.
'''

def canFinish(numCourses, prerequisites):
    visited = []
    my_dict = {}
    c = 0
    for (a, b) in prerequisites:
        if (b, a) in visited:
            return False
        if (a, b) in visited:
            continue
        if a not in my_dict:
            my_dict[a] = 1
            c += 1
        if b not in my_dict:
            my_dict[b] = 1
            c += 1
        visited.append((a, b))
    # print(c)
    if c <= numCourses:
        return True
    return False

# not solved
# graph if has cycle, adjacent list representation
# leetcode's solution
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    from collections import defaultdict
    courseDict = defaultdict(list)

    for relation in prerequisites:
        nextCourse, prevCourse = relation[0], relation[1]
        courseDict[prevCourse].append(nextCourse)
    print(courseDict)
    path = [False] * numCourses
    checked = [False] * numCourses
    for currCourse in range(numCourses):
        if isCyclic(currCourse, courseDict, checked, path):
            return False
    return True


def isCyclic(currCourse, courseDict, path):
    """
    backtracking method to check that no cycle would be formed starting from currCourse
    """
    print(currCourse)

     # 1). bottom-cases
    if checked[currCourse]:
        # this node has been checked, no cycle would be formed with this node.
        return False

    if path[currCourse]:
        print('yes')
        # come across a previously visited node, i.e. detect the cycle
        return True

    # 2). postorder DFS on the children nodes
    # mark the node in the path
    path[currCourse] = True

    # postorder DFS, to visit all its children first.
    ret = False
    for child in courseDict[currCourse]:
        ret = isCyclic(child, courseDict, checked, path)
        if ret: break

    # 3). after the visits of children, we come back to process the node itself
    # remove the node from the path
    path[currCourse] = False
    print(path)
    
    # Now that we've visited the nodes in the downstream,
    #   we complete the check of this node.
    checked[currCourse] = True

    # print(ret)
    return ret

# topological sort
class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    from collections import defaultdict, deque
    # key: index of node; value: GNode
    graph = defaultdict(GNode)

    totalDeps = 0
    for relation in prerequisites:
        nextCourse, prevCourse = relation[0], relation[1]
        graph[prevCourse].outNodes.append(nextCourse)
        graph[nextCourse].inDegrees += 1
        totalDeps += 1

    # we start from courses that have no prerequisites.
    # we could use either set, stack or queue to keep track of courses with no dependence.
    nodepCourses = deque()
    for index, node in graph.items():
        # print(index, node.inDegrees)
        # print(index, node.outNodes)
        if node.inDegrees == 0:
            nodepCourses.append(index)

    removedEdges = 0
    while nodepCourses:
        # pop out course without dependency
        course = nodepCourses.pop()

        # remove its outgoing edges one by one
        for nextCourse in graph[course].outNodes:
            graph[nextCourse].inDegrees -= 1
            removedEdges += 1
            # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
            if graph[nextCourse].inDegrees == 0:
                nodepCourses.append(nextCourse)

    if removedEdges == totalDeps:
        return True
    else:
        # if there are still some edges left, then there exist some cycles
        # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
        return False

# numCourses = 2
# prerequisites = [[1,0]]
# print(canFinish(numCourses, prerequisites))
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))
