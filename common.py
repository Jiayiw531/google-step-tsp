def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))


def print_tour(tour):
    print(format_tour(tour))

def total_distance(tour, dist): 
    total = 0
    N = len(tour) 
    for i in range(N):
        total += dist[tour[i]][tour[(i + 1) % N]]
    return total