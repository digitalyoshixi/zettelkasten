---
tags:
  - ctf
---
This program is impossible to reverse, since you are using [[SHA256]].
The hint in this challenge says that we need to find the shortest path.
We have a script to find the shortest path:
```
import numpy as np
import itertools

def solve_tsp_dynamic(distances):
    """
    Implementation of the Held-Karp algorithm for solving the TSP problem
    using dynamic programming.
    """
    n = distances.shape[0]
    
    # Maps each subset of the nodes (as a bit mask) to the cost to reach that subset
    # and the last node used to reach it: (cost, prev_node)
    C = {}
    
    # Initialize: cost to reach node i from start node 0
    for i in range(1, n):
        C[(1 << i, i)] = (distances[0][i], 0)
    
    # Iterate over all subsets of nodes of increasing size
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Convert subset to bit mask representation
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            
            # Find the lowest cost to get to this subset
            for last in subset:
                prev = bits & ~(1 << last)  # All nodes in this subset except last
                if (prev, last) not in C:
                    continue
                    
                res = []
                for prev_last in subset:
                    if prev_last == last:
                        continue
                    if (prev, prev_last) in C:
                        res.append((C[(prev, prev_last)][0] + distances[prev_last][last], prev_last))
                
                if res:
                    C[(bits, last)] = min(res)
    
    # Find optimal cost from all subsets with all bits set
    bits = (1 << n) - 2  # All nodes except 0
    res = []
    for last in range(1, n):
        if (bits, last) in C:
            res.append((C[(bits, last)][0] + distances[last][0], last))
    
    # Get the overall optimal cost and the last node in the path
    opt, last = min(res)
    
    # Backtrack to find the optimal path
    path = [0]
    mask = (1 << n) - 2  # All nodes except 0
    
    for i in range(n - 1):
        path.append(last)
        new_mask = mask & ~(1 << last)
        _, last = C[(mask, last)]
        mask = new_mask
    
    path.append(0)  # Return to start
    
    return opt, list(reversed(path))

# Use the distances matrix provided
distances = np.array([
    [0, 27207933, 29257191, 30767375, 33358061, 31710853, 18267351, 28646422, 25181575, 32668955, 31721351, 31311914, 17436287, 31231519, 27398390, 26665226, 33405147, 29479064, 28859609, 32875400],
    [27207933, 0, 18723267, 27461140, 27706598, 17153389, 26073565, 31907885, 30552119, 31028215, 32910477, 33323884, 31917434, 32961668, 32744601, 32930203, 33402104, 29926349, 26989354, 28354374],
    [29257191, 18723267, 0, 26971581, 30094007, 26800381, 25822626, 31797481, 30354002, 29221683, 26252638, 25958512, 30021148, 26305193, 32130369, 17552296, 28667078, 30263697, 27936885, 25722954],
    [30767375, 27461140, 26971581, 0, 31156816, 30331322, 28073673, 26204203, 18396217, 25838588, 16791286, 26131377, 29700497, 27798881, 33059254, 29477864, 29721951, 29439773, 27739929, 30777073],
    [33358061, 27706598, 30094007, 31156816, 0, 27346875, 16937956, 32281098, 30112898, 27364910, 30685671, 33231675, 28723588, 31226010, 30541690, 25856444, 31229621, 31201226, 17392801, 27161053],
    [31710853, 17153389, 26800381, 30331322, 27346875, 0, 27018180, 26738900, 28340609, 26024216, 31493000, 17879357, 33432247, 26366524, 28566084, 30498671, 27754527, 30294100, 25178897, 25771567],
    [18267351, 26073565, 25822626, 28073673, 16937956, 27018180, 0, 25268124, 32590760, 27138017, 32999152, 26220279, 26204222, 27031462, 25273715, 25443122, 28617815, 27829458, 29730434, 29457736],
    [28646422, 31907885, 31797481, 26204203, 32281098, 26738900, 25268124, 0, 25545320, 33382954, 31145177, 27664100, 32470009, 27768727, 27949390, 27242094, 28136501, 18433903, 31905380, 18428695],
    [25181575, 30552119, 30354002, 18396217, 30112898, 28340609, 32590760, 25545320, 0, 27003713, 25437214, 31796476, 32892705, 25571056, 29517404, 29493907, 17863705, 30959457, 29889268, 30146332],
    [32668955, 31028215, 29221683, 25838588, 27364910, 26024216, 27138017, 33382954, 27003713, 0, 18199400, 27564338, 29696304, 17432494, 29903977, 25517772, 27950322, 31033257, 25934690, 27689266],
    [31721351, 32910477, 26252638, 16791286, 30685671, 31493000, 32999152, 31145177, 25437214, 18199400, 0, 25876546, 31958139, 27864810, 28321738, 32744171, 30132076, 26162759, 30621460, 26660593],
    [31311914, 33323884, 25958512, 26131377, 33231675, 17879357, 26220279, 27664100, 31796476, 27564338, 25876546, 0, 28787506, 26446653, 18665171, 26795144, 28330910, 27423379, 31975694, 29184736],
    [17436287, 31917434, 30021148, 29700497, 28723588, 33432247, 26204222, 32470009, 32892705, 29696304, 31958139, 28787506, 0, 30143172, 25912069, 18840703, 26932680, 31591461, 25437981, 31899333],
    [31231519, 32961668, 26305193, 27798881, 31226010, 26366524, 27031462, 27768727, 25571056, 17432494, 27864810, 26446653, 30143172, 0, 31608667, 32254626, 33332666, 28876524, 33245767, 18585598],
    [27398390, 32744601, 32130369, 33059254, 30541690, 28566084, 25273715, 27949390, 29517404, 29903977, 28321738, 18665171, 25912069, 31608667, 0, 32919698, 31369881, 17023154, 28664099, 32553702],
    [26665226, 32930203, 17552296, 29477864, 25856444, 30498671, 25443122, 27242094, 29493907, 25517772, 32744171, 26795144, 18840703, 32254626, 32919698, 0, 32324337, 31222350, 27812923, 28001748],
    [33405147, 33402104, 28667078, 29721951, 31229621, 27754527, 28617815, 28136501, 17863705, 27950322, 30132076, 28330910, 26932680, 33332666, 31369881, 32324337, 0, 26022470, 18709664, 29315967],
    [29479064, 29926349, 30263697, 29439773, 31201226, 30294100, 27829458, 18433903, 30959457, 31033257, 26162759, 27423379, 31591461, 28876524, 17023154, 31222350, 26022470, 0, 29138946, 27237135],
    [28859609, 26989354, 27936885, 27739929, 17392801, 25178897, 29730434, 31905380, 29889268, 25934690, 30621460, 31975694, 25437981, 33245767, 28664099, 27812923, 18709664, 29138946, 0, 30105348],
    [32875400, 28354374, 25722954, 30777073, 27161053, 25771567, 29457736, 18428695, 30146332, 27689266, 26660593, 29184736, 31899333, 18585598, 32553702, 28001748, 29315967, 27237135, 30105348, 0]
])

# However, the exact algorithm will likely exceed memory limits for n=20
# Let's use a heuristic approach - Nearest Neighbor

def nearest_neighbor_tsp(distances, start=0):
    """
    Implementation of the nearest neighbor heuristic for TSP.
    """
    n = distances.shape[0]
    path = [start]
    unvisited = set(range(n))
    unvisited.remove(start)
    total_distance = 0
    
    curr = start
    while unvisited:
        next_node = min(unvisited, key=lambda x: distances[curr][x])
        unvisited.remove(next_node)
        path.append(next_node)
        total_distance += distances[curr][next_node]
        curr = next_node
    
    # Return to start
    path.append(start)
    total_distance += distances[curr][start]
    
    return total_distance, path

# Let's also implement 2-opt local search to improve the nearest neighbor solution
def two_opt(route, distances):
    """
    2-opt local search for TSP.
    """
    improvement = True
    route = route[:-1]  # Remove the last node (which is the same as the first)
    best_distance = calculate_path_distance(route + [route[0]], distances)
    
    while improvement:
        improvement = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # Skip adjacent edges
                
                # Create new route with 2-opt swap
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_distance = calculate_path_distance(new_route + [new_route[0]], distances)
                
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
                    improvement = True
                    break
            if improvement:
                break
    
    return best_distance, route + [route[0]]

def calculate_path_distance(path, distances):
    """
    Calculate the total distance of a path.
    """
    return sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))

# Due to memory constraints with n=20, let's use the nearest neighbor approach with 2-opt improvement
nn_distance, nn_path = nearest_neighbor_tsp(distances)
improved_distance, improved_path = two_opt(nn_path, distances)

print(f"Nearest Neighbor solution:")
print(f"Path: {nn_path}")
print(f"Total distance: {nn_distance}")
print("\n2-opt improved solution:")
print(f"Path: {improved_path}")
print(f"Total distance: {improved_distance}")

# For completeness, let's try to solve a smaller subset with the exact algorithm
# to demonstrate how it works
def solve_small_subset():
    # Take first 10 nodes only for demonstration
    small_distances = distances[:10, :10]
    opt_distance, opt_path = solve_tsp_dynamic(small_distances)
    print("\nExact solution for first 10 nodes:")
    print(f"Path: {opt_path}")
    print(f"Total distance: {opt_distance}")

# Uncomment this to run the exact algorithm on a smaller subset
# solve_small_subset()

# Run the full nearest neighbor with 2-opt improvement
nn_distance, nn_path = nearest_neighbor_tsp(distances)
print(f"Nearest Neighbor solution:")
print(f"Path: {nn_path}")
print(f"Total distance: {nn_distance}")

# Time to run 2-opt improvement might be long, so let's implement a limited version
def limited_two_opt(route, distances, max_iterations=1000):
    """
    2-opt local search for TSP with a limit on iterations to ensure reasonable runtime.
    """
    improvement = True
    route = route[:-1]  # Remove the last node (which is the same as the first)
    best_distance = calculate_path_distance(route + [route[0]], distances)
    iterations = 0
    
    while improvement and iterations < max_iterations:
        improvement = False
        iterations += 1
        
        # Instead of checking all possible combinations, randomly sample some pairs
        # This makes the algorithm faster for large instances
        pairs = [(i, j) for i in range(1, len(route) - 1) for j in range(i + 2, len(route))]
        np.random.shuffle(pairs)
        # Limit the number of pairs we check per iteration
        for i, j in pairs[:min(100, len(pairs))]:
            # Create new route with 2-opt swap
            new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
            new_distance = calculate_path_distance(new_route + [new_route[0]], distances)
            
            if new_distance < best_distance:
                route = new_route
                best_distance = new_distance
                improvement = True
                break
    
    return best_distance, route + [route[0]]

# Run limited 2-opt improvement
np.random.seed(42)  # For reproducibility
improved_distance, improved_path = limited_two_opt(nn_path, distances)
print("\n2-opt improved solution:")
print(f"Path: {improved_path}")
print(f"Total distance: {improved_distance}")
```
Then, we get this list of paths: `[0, 12, 15, 2, 1, 5, 11, 14, 17, 7, 19, 13, 9, 10, 3, 8, 16, 18, 4, 6, 0]`
![[BreakTheSyntax2025 Rainbom Bash Adventure-20250510155430327.webp]]
We will hard-code these nodes.
![[BreakTheSyntax2025 Rainbom Bash Adventure-20250510155314050.webp]]