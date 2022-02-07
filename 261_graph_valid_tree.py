def validTree(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    dic = defaultdict(list)
    for A, B in edges:
        dic[A].append(B)
        dic[B].append(A)

        # print(dic)
    visited = set()
    '''
    On an undirected graph, like the one we're working with here, 
    trivial "cycles" will be detected. 
    Most rely on the idea that a depth-first search should only go along each edge once, 
    and therefore only in one direction.
    
    Then, when we iterate through the neighbours of a node, 
    we ignore the "parent" node as otherwise it'll be detected as a trivial cycle 
    (and we know that the parent node has already been visited by this point anyway). 
    The starting node (0 in this implementation) has no "parent", so put it as -1.
    '''
    def DFS(v, parent):
        if v in visited: return
        visited.add(v)            # mark the current node as visited
        # print(v, end=' ')               # print the current node

        # do for every edge (v, u)
        for neighbor in dic[v]:
            if neighbor == parent:
                continue
            if neighbor in visited: 
                return False
            result = DFS(neighbor, v)
            if not result: return False
        return True

    return DFS(0, -1) and len(visited) == n
    
    '''
    On the plus side, we can use a simple seen set and just pass a parent parameter. 
    This makes the code a bit simpler!

    '''
