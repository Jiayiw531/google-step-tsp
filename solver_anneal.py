#!/usr/bin/env python3

import sys
import math
import os
import random

from common import print_tour, read_input, total_distance


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# returns the tour array after swap is made
# uses index{1,2} to represent city index, to differ from city{1,2} which represented their (x,y) positions
def swap(tour, index1, index2): 
    if index1 + 1 >= len(tour) or index2 + 1 >= len(tour): 
        return tour
    
    # make sure index 1 is always to the left of 2
    if index1 > index2: 
        index1, index2 = index2, index1 

    # create new tour by reversing the route between index 1 and 2
    new_tour = tour[: index1 + 1] + tour[index2 : index1 : -1] + tour[index2 + 1 :]
    
    return new_tour

def solve(cities):
    N = len(cities)
    temp = 1
    cooling_factor = 0.98

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    # start with a random tour
    tour = [0] + random.sample(range(1, N), N - 1)

    shortest_tour = list(tour)
    
    while temp > 0.001: 
        # randomly select two indices to swap
        index1 = random.randint(0, N - 1)
        index2 = random.randint(0, N - 1)
        while index1 == index2:  # ensure indices are different
            index2 = random.randint(0, N - 1)
        # swap the two indices in the tour
        tour = swap(list(range(N)), index1, index2)
        # calculate the total distance of the new tour
        curr_total_distance = total_distance(tour, [[distance(cities[i], cities[j]) for j in range(N)] for i in range(N)])
        # calculate the difference in distance
        diff = curr_total_distance - total_distance(shortest_tour, dist)
        # if the new tour is shorter, or if we accept a longer tour based on temperature
        if diff < 0 or random.random() < math.exp(-diff / temp):
            shortest_tour = tour
            print("New tour found with distance:", curr_total_distance)
        # cool down the temperature
        temp *= cooling_factor

    curr_total_distance = total_distance(shortest_tour, dist)
    improving = True

    # end the loop when tour is not improving
    while improving: 
        improving = False
        for i in range(len(shortest_tour) - 1): # i is index of the starting point, so ends at the second last city
            for j in range(i + 1, len(shortest_tour)): # j is the end point index, starts behind i by 1, ends at last city in tour
                
                # make sure i and j are not adjacent / the same
                if j == i + 1 or (i == 0 and j == N - 1): 
                    continue
                
                city_i = shortest_tour[i]
                city_i_next = shortest_tour[(i + 1) % N]
                city_j = shortest_tour[j]
                city_j_next = shortest_tour[(j + 1) % N]

                # if the new way of connection : i to j and i_nxt to j_nxt
                # results in a smaller total distance (diff < 0), perform the swap
                diff = (dist[city_i][city_j] + dist[city_i_next][city_j_next]) - \
                       (dist[city_i][city_i_next] + dist[city_j][city_j_next])
                if diff < 0: 
                    # replace the previous segment between i+1 and j+1 to the reversed segment between i and j
                    shortest_tour[i+1 : j+1] = shortest_tour[j : i : -1]
                    curr_total_distance += diff
                    improving = True
                    break
            if improving: 
                break

    print("shortest_tour total distance: ", total_distance(shortest_tour, dist))
    print("verifier output:", sum(distance(cities[shortest_tour[i]], cities[shortest_tour[(i + 1) % N]])
                              for i in range(N)))
    return shortest_tour

def write_output(tour, output_filename): 
    with open(output_filename, 'w') as f:
        f.write("index\n")
        for city_index in tour:
            f.write(f"{city_index}\n")

if __name__ == '__main__':
    assert len(sys.argv) > 1
    input_filename = sys.argv[1]
    tour = solve(read_input(input_filename))

    # get challenge number from input filename
    base_name = os.path.basename(input_filename)
    input_prefix = os.path.splitext(base_name)[0]

    assert('_' in input_prefix)
    output_filename = "anneal_output_" + input_prefix.split("_")[-1] + ".csv"

    write_output(tour, output_filename)

    print("tour saved to", output_filename)