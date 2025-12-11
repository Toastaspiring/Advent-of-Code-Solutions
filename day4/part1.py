def solve_forklift_puzzle(filename):
    # Read the grid from the file
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    # Directions for the 8 neighbors (dx, dy)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            # We only care if the current spot is a roll of paper (@)
            if grid[r][c] == '@':
                neighbor_rolls = 0
                
                # Check all 8 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if neighbor is within bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbor_rolls += 1
                
                # Condition: accessible if fewer than 4 adjacent rolls
                if neighbor_rolls < 4:
                    accessible_count += 1

    return accessible_count

if __name__ == "__main__":
    result = solve_forklift_puzzle('input.txt')
    print(f"Accessible paper rolls: {result}")