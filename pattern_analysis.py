"""
Pattern & Remainder Distribution Analyzer
-----------------------------------------
Analyzes the frequency of each remainder per row in Pascal's triangle mod n,
mirroring algebraic term tracking.
"""

from pascals_mod import generate_pascals_mod

def analyze_remainder_distribution(num_rows, mod):
    triangle = generate_pascals_mod(num_rows, mod)
    
    print(f"\n--- Remainder Frequency Analysis (Mod {mod}) ---")
    print(f"{'Row':<5} | {'Total Elements':<15} | {'Remainder Counts (R:0, R:1, ...)'}")
    print("-" * 65)
    
    for i, row in enumerate(triangle):
        counts = {r: 0 for r in range(mod)}
        for val in row:
            counts[val] += 1
            
        count_str = ", ".join([f"R:{r}={counts[r]}" for r in range(mod)])
        print(f"{i:<5} | {len(row):<15} | {count_str}")

if __name__ == "__main__":
    # Run analysis for Mod 3 up to row 15
    analyze_remainder_distribution(15, 3)
