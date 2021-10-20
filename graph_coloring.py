'''Adapted from mohit kumar 29's solution on Geeks for Geeks
(https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/)
'''

def add_edge(adjacent, v, w):
    '''
    inputs: adj, the adjacency list. a list of lists containing the adjacency for every vertex
            v, the first node
            w, the second node
    An edge will be added between the nodes v and w by updating the adjacency matrix.
    '''
    adjacent[v].append(w)
    adjacent[w].append(v)
    return adjacent

def color(adjacent, V):
    '''
    A simple algorithm that colors a graph. Does not necessarily give the most optimal solution.
    inputs: adj, an adjacency matrix
            V, the number of vertices in the graph
     '''
    result = [-1] * V # create results matrix of all -1

    # Assign first color to first vertex. Each color is represented by a positive integer.
    result[0] = 0

    # A temporary array that stores the available colors.
    # If False, then that color has been assigned to an adjacent vertex and cannot be used to color the current vertex
    ok_colors = [True] * V

    # Assign colors to remaining vertices
    for vertex in range(1, V):
        # checks all adjacent vertices to u
        for i in adjacent[vertex]:
            # if an adjacent vertex already has a color, then the current vertex can't use the same color.
            if result[i] != -1:
                ok_colors[result[i]] = False
        color = 0
        while color < V:
            #if there is an available color, then we break the while loop. If not, we check the next color
            if ok_colors[color] == True:
                break
            color += 1

        #assign a coloring to that vertex
        result[vertex] = color

        # check all adjacent vertices of current vertex
        for adj_v in adjacent[vertex]:
            # if the vertex is not already colored
            if result[adj_v] != -1:
                # make it so that vertex can't have the same coloring as the current vertex
                ok_colors[result[adj_v]] = True

    for node in range(V):
        print("Vertex with edges to", adjacent[node], " ---> Color", result[node])

def welsh_powell(adjacent, V):
    ''' Sorts nodes by length
    '''
    print('og', adjacent)
    adjacent.sort(key = len, reverse = True)
    print('sorted',adjacent)
    color(adjacent, V)


if __name__ == '__main__':

    g1 = [[] for i in range(5)]
    g1 = add_edge(g1, 0, 1)
    g1 = add_edge(g1, 0, 2)
    g1 = add_edge(g1, 1, 2)
    g1 = add_edge(g1, 1, 3)
    g1 = add_edge(g1, 2, 3)
    g1 = add_edge(g1, 3, 4)
    print("Coloring of graph 1 ")
    color(g1, 5)

    g2 = [[] for i in range(5)]
    g2 = add_edge(g2, 0, 1)
    g2 = add_edge(g2, 0, 2)
    g2 = add_edge(g2, 1, 2)
    g2 = add_edge(g2, 1, 4)
    g2 = add_edge(g2, 2, 4)
    g2 = add_edge(g2, 4, 3)
    print("\nColoring of graph 2")
    color(g2, 5)
    print("\Welsh-Powell Coloring of graph 2")
    welsh_powell(g2, 5)
