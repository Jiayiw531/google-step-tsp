# Solution descriptions

### Very helpful universal optimization technique inspired by [Emmanual's blog][https://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/]
- total distance also does not need to be calculated everytime a swap is performed; would be much more efficient if only the swapped sections were compared



## solver_greedy_2-opt
- based on greedy approach already implemented, incorporated 2-opt to optimize possible entanglements in the designated route found by greedy algorithm
- 2-opt swap reverses the route between two given vertices, and checks if the routes could be shortened with this approach
- performs 2-opt swaps on every pair of vertices on the route to see if the route could be optimized

## 焼きなまし法 / Simulated Annealing Heuristic
based on the idea from [Emmanuel's blog on simulted annealing and its application to traveling salesman problem](https://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/)
- uses a concept of *temperature* to decide when to terminate optimization loop
- *temperature* is lowered each iteration by a multiplying to a *cooling_factor* 
- worth to note: a probability variable that keeps the possibility of keeping a longer new path
- cities list gets shuffled so the traversing direction is decided randomly
- for each iteration: 
  - swap two cities and see if new path is shorter
    - shorter: 100% new_path gets kept
    - not shorter: by certain probability new_path is kept
  - cool down temperature

# algorithm inspirations

from Google STEP course materials

- 2.5 opt
- 3 opt
- 焼きなまし法
- 遺伝的アルゴリズム
- 蟻コロニー最適化


# Acknowledgements
## 2-opt
- The idea and workflow of 2-opt were learned from [Wikipedia](https://en.wikipedia.org/wiki/2-opt)
## Simulated Annealing
- Idea comes from [codeCapsule by Emmanuel Goossaert](https://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/)