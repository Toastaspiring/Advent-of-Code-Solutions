def solve_forklift_simulation(filename):
    # Read the grid into a mutable list of lists
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0

    # Directions for the 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while True:
        # List to store coordinates of rolls to be removed in this round
        to_remove = []

        # Scan the entire grid
        for r in range(rows):
            for c in range(cols):
                # We only check existing paper rolls
                if grid[r][c] == '@':
                    neighbor_rolls = 0
                    
                    # Count adjacent paper rolls
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        # Check bounds
                        if 0 <= nr < rows and 0 <= nc < cols:
                            # Only count if it's currently a roll ('@')
                            # Removed rolls ('.') do not count as obstacles
                            if grid[nr][nc] == '@':
                                neighbor_rolls += 1
                    
                    # If fewer than 4 neighbors, it's accessible
                    if neighbor_rolls < 4:
                        to_remove.append((r, c))

        # If no rolls can be removed this round, we are done
        if not to_remove:
            break

        # Remove the rolls from the grid (update state for next iteration)
        for r, c in to_remove:
            grid[r][c] = '.' # Mark as empty space
            
        total_removed += len(to_remove)
        # print(f"Round complete: removed {len(to_remove)} rolls.")

    return total_removed

if __name__ == "__main__":
    result = solve_forklift_simulation('input.txt')
    print(f"Total paper rolls removed: {result}")