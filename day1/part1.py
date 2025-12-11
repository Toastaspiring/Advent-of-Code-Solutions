def solve_safe(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            rotations = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find {filename}. Make sure it is in the same directory.")
        return

    current_pos = 50
    zero_count = 0
    total_positions = 100

    print(f"Starting position: {current_pos}")
    print(f"Processing {len(rotations)} rotations...")

    for rotation in rotations:
        direction = rotation[0].upper()
        try:
            distance = int(rotation[1:])
        except ValueError:
            print(f"Skipping invalid line: {rotation}")
            continue

        if direction == 'R':
            # Rotate right (add)
            current_pos = (current_pos + distance) % total_positions
        elif direction == 'L':
            # Rotate left (subtract)
            # Python's modulo operator handles negatives correctly for this puzzle
            # e.g., -5 % 100 = 95
            current_pos = (current_pos - distance) % total_positions
        
        # Check if the dial is pointing at 0
        if current_pos == 0:
            zero_count += 1

    print("-" * 30)
    print(f"Final Dial Position: {current_pos}")
    print(f"The actual password (Part 1) is: {zero_count}")

if __name__ == "__main__":
    solve_safe()