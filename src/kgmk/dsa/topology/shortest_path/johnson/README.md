# Johnson shotest dist 

# keywords 
- potential
- negative edges

# summary 
1. add super node and edges.
2. bellman ford from super node and get potential of each node.
3. dijkstra from each node.
4. retrieve real distances.


# note 
- sparse graph 
- all source shortest path


# time complexity 
- $O(EV + VE\log{V} + V^2)$