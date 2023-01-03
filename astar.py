def astar(star_node,stop_node):
    open_set=set(star_node)
    closed_set=set()
    g={}
    parent={}
    
    g[star_node]=0
    parent[star_node]=star_node
    while len(open_set)>0:
        n=None
        for v in open_set:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        if n==stop_node or graph_nodes[n]==None:
            pass
        else:
            for(m,weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                        
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n==None:
            print("path doesnot exits")
            return None
        if n==stop_node:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(star_node)
            path.reverse()
            print('path:{}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print("path doesnot exist")
    return None

def get_neighbours(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None
def heuristic(n):
    H_dist={
        'A':11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0,

    }
    return H_dist[n]
graph_nodes={
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',7)],
 
    'D':[('G',1)],
    'E':[('D',5)],
    }
astar('A','G')
    
