def bfs(graph,start_node):
    visited=[]
    queue=[start_node]
    while queue:
        current_node=queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
        for neighbour in graph.get(current_node,[]):
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)       
    return visited
def search(item):    
   a=bfs(student_graph,start)
   b=[]
   c=False
   for i in range(len(a)):       
        if (item==a[i]):
                b.append(a[i])
                c=True             
                break               
        else:
            b.append(a[i])
   if c==True:
        return print("target is found and list is",b)  
   else:
        return print("target is  not found ")  
    




print(".......build your graph.......")
student_graph={}
edges=int(input("enter number of edges you need :"))
for i in range(edges):
    u,v=input(f"edes{i+1}:").split()
    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph:
        student_graph[v]=[]        
    student_graph[u].append(v)
    student_graph[v].append(u)
start=input("enter your start node : ")
print("graph:-",student_graph)
target=input("entes your target item in a graph:")
a=bfs(student_graph,start)
print("visited list:",a)
b=search(target)
