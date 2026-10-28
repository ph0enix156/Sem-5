
# Map Colouring using CSP (Backtracking)

# Regions and their neighbouring regions
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colours
colours = ['Red', 'Green', 'Blue']

# Store assigned colours
colour_map = {}


def is_valid(region, colour):
    for neighbour in graph[region]:
        if colour_map.get(neighbour) == colour:
            return False
    return True


def solve():
    if len(colour_map) == len(graph):
        return True

    # Select an uncoloured region
    region = next(r for r in graph if r not in colour_map)

    # Try each available colour
    for colour in colours:
        if is_valid(region, colour):
            colour_map[region] = colour

            if solve():
                return True

            # Backtracking
            del colour_map[region]

    return False


if solve():
    print("Map Colouring Solution:")
    for region, colour in colour_map.items():
        print(region, ":", colour)
else:
    print("No solution exists")
