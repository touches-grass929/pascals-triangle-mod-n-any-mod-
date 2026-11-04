"""
Pascal's Triangle Modulo n Generator
-------------------------------------
Generates Pascal's triangle up to 'num_rows' modulo 'mod', 
with options for textual or custom symbol visualization.
"""

def generate_pascals_mod(num_rows, mod):
    """Generates Pascal's triangle up to num_rows modulo n."""
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = (triangle[i - 1][j - 1] + triangle[i - 1][j]) % mod
        triangle.append(row)
    return triangle

def print_mod_triangle(triangle, mod):
    """Pretty prints the triangle with symbols based on remainders."""
    num_rows = len(triangle)
    
    # Define symbols for remainders (customizable for mod 3 or others)
    symbols = {
        0: "░░",  # Remainder 0 (shaded/hatched in notebook)
        1: "██",  # Remainder 1 (yellow)
        2: "▒▒"   # Remainder 2 (pink/red)
    } if mod == 3 else {0: ". ", int_val: f"{int_val} " for int_val in range(1, mod)}

    print(f"\n--- Pascal's Triangle Mod {mod} ({num_rows} Rows) ---")
    for i, row in enumerate(triangle):
        if mod == 3:
            row_str = "".join(symbols.get(x, f"{x} ") for x in row)
        else:
            row_str = " ".join(str(x) for x in row)
            
        # Center alignment for pyramid shape
        padding = " " * (num_rows - i - 1) * (2 if mod == 3 else 1)
        print(padding + row_str)

if __name__ == "__main__":
    # Example 1: Mod 3 (matching your notebook exploration)
    mod3_triangle = generate_pascals_mod(16, 3)
    print_mod_triangle(mod3_triangle, 3)
    
    # Example 2: Mod 2 (Sierpinski Triangle)
    sierpinski = generate_pascals_mod(16, 2)
    print("\n--- Sierpinski Triangle (Mod 2) ---")
    for i, row in enumerate(sierpinski):
        row_str = "".join("▲ " if x == 1 else "  " for x in row)
        print(" " * (16 - i - 1) + row_str)
