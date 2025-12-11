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

        needed_after = k - 1 - i
        

        end_limit = n - needed_after
        

        search_window = digits[current_start : end_limit]
        
        best_digit = max(search_window)
        

        relative_idx = search_window.index(best_digit)
        actual_idx = current_start + relative_idx
        
        result_digits.append(best_digit)
        

        current_start = actual_idx + 1
        
    
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