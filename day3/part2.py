def calculate_max_joltage(line, k=12):
    line = line.strip()
    if not line:
        return 0
    
    digits = [int(c) for c in line]
    n = len(digits)
    
    if n < k:
        return 0
    
    current_start = 0
    result_digits = []
    
    for i in range(k):
        # Number of digits needed AFTER this one to complete the sequence of 12
        needed_after = k - 1 - i
        
        # We must pick a digit such that we have at least 'needed_after' digits remaining.
        # The last possible index we can pick is n - 1 - needed_after.
        # The slice upper bound (exclusive) is n - needed_after.
        end_limit = n - needed_after
        
        # Search for the best digit in the valid window
        search_window = digits[current_start : end_limit]
        
        # Greedy choice: 
        # 1. Pick the largest digit available.
        # 2. If there are multiple, picking the first one is always optimal 
        #    because it leaves the largest possible suffix for the remaining steps.
        best_digit = max(search_window)
        
        # Find the index of the first occurrence in the window
        relative_idx = search_window.index(best_digit)
        actual_idx = current_start + relative_idx
        
        result_digits.append(best_digit)
        
        # Move start pointer to just after the chosen digit
        current_start = actual_idx + 1
        
    # Convert the list of digits into a single integer
    result_val = int("".join(map(str, result_digits)))
    return result_val

def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            
        total_joltage = 0
        for line in lines:
            line = line.strip()
            if line:
                val = calculate_max_joltage(line)
                total_joltage += val
                
        print(f"Total Output Joltage: {total_joltage}")
        
    except FileNotFoundError:
        print("Error: input.txt not found.")

if __name__ == "__main__":
    main()