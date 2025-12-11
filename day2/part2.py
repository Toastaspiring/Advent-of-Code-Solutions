import os

def is_invalid_id(n):
    """
    Checks if an ID is invalid based on Part 2 rules:
    It is invalid if it is made only of some sequence of digits repeated at least twice.
    """
    s = str(n)
    length = len(s)
    
    # We try all possible lengths for the repeating pattern (p_len).
    # The pattern length must be at least 1 and at most length // 2.
    for p_len in range(1, length // 2 + 1):
        # The total length must be divisible by the pattern length
        if length % p_len == 0:
            pattern = s[:p_len]
            multiplier = length // p_len
            
            # Check if the pattern repeated matches the original string
            if pattern * multiplier == s:
                return True
                
    return False

def solve_ranges(input_data):
    total_sum = 0
    
    # Normalize input: replace commas with newlines to handle comma-separated lists
    # This allows the function to work with both "1-2\n3-4" and "1-2,3-4"
    normalized_data = input_data.replace(',', '\n')
    lines = normalized_data.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split('-')
        if len(parts) != 2:
            continue
            
        start = int(parts[0])
        end = int(parts[1])
        
        # Ranges are inclusive
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num
                
    return total_sum

# --- Test with the example provided in the prompt ---
example_input = """
11-22
95-115
998-1012
1188511880-1188511890
222220-222224
1698522-1698528
446443-446449
38593856-38593862
565653-565659
824824821-824824827
2121212118-2121212124
"""

print("--- Running Example Case ---")
result = solve_ranges(example_input)
print(f"Calculated Sum: {result}")
expected = 4174379265
if result == expected:
    print("✅ Example passed!")
else:
    print(f"❌ Example failed. Expected {expected}")

# --- Actual Input Section ---
print("\n--- Running Actual Input ---")

# Try to read from input.txt if it exists
if os.path.exists('input.txt'):
    with open('input.txt', 'r') as f:
        file_content = f.read()
    print("Reading from input.txt...")
    print(f"Total Sum: {solve_ranges(file_content)}")
else:
    # Fallback if file is not found
    print("⚠️ input.txt not found. Please ensure the file is in the same directory.")
    # You can also manually paste the comma-separated string here if needed:
    # manual_input = "18623-26004,226779-293422,..."
    # print(f"Total Sum (Manual): {solve_ranges(manual_input)}")