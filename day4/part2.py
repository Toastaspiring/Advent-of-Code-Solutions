def solve_forklift_simulation(filename):

    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0


    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while True:

        to_remove = []

        # Scan the entire grid
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '@':
                    neighbor_rolls = 0
                    

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        

                        if 0 <= nr < rows and 0 <= nc < cols:

                            if grid[nr][nc] == '@':
                                neighbor_rolls += 1
                    

                    if neighbor_rolls < 4:
                        to_remove.append((r, c))


        if not to_remove:
            break


        for r, c in to_remove:
            grid[r][c] = '.'
            
        total_removed += len(to_remove)


    return total_removed

if __name__ == "__main__":
    result = solve_forklift_simulation('input.txt')
    print(f"Total paper rolls removed: {result}")