def calculate_max_joltage(line):
    line = line.strip()
    if not line:
        return 0
    
    digits = [int(c) for c in line]
    n = len(digits)
    
    # We want to maximize the number formed by digits[i] and digits[j] where i < j.
    # The number is digits[i] * 10 + digits[j].
    
    # Iterate through possible first digits from 9 down to 1
    for first_digit_val in range(9, 0, -1):
        # Find all indices where this digit appears and has a successor
        indices = [i for i, d in enumerate(digits) if d == first_digit_val and i < n - 1]
        
        if not indices:
            continue
            
        # If we found at least one valid starting position for this digit,
        # we know this is the best possible 'tens' place we can get.
        # Now we just need to find the best 'ones' place that follows it.
        
        max_pair_val = -1
        
        for idx in indices:
            # Look at all digits after this index
            following_digits = digits[idx+1:]
            max_next = max(following_digits)
            pair_val = first_digit_val * 10 + max_next
            
            if pair_val > max_pair_val:
                max_pair_val = pair_val
        
        return max_pair_val
        
    return 0

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