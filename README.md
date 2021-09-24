# Dijkstra_Shortest_Path

Dijsktra's algorithm is applicable for directed and undirected graphs where the graph is connected and all edges have nonnegative weights.

![graph network](/images/graphnetimage.png)

### Procedure

Step 1: Create a list to keep track of the minimum distance and set the distance of the source to 0 and the remaining nodes to infinity.
Step 2: Set the source as the current node.
Step 3: Update the current node as visited with the help of a set to keep track.
Step 4: For all nodes adjacent to the current node, set the distance from the source to the adjacent node equal to the minimum of its present distance and the sum of the weight of the current node and the distance from the source to the current node.
Step 5: From the set of unvisited nodes, select the node with the minimum weight edge from a visited node to be the current node using a priority queue.
Step 6: Repeated step 3-5 until all nodes are visited.

![animated dijkstra](https://commons.wikimedia.org/wiki/File:DijkstraDemo.gif#/media/File:DijkstraDemo.gif)


