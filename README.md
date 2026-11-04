# Pascal's Triangle Modulo $n$ & Fractal Patterns

An exploration of Pascal's triangle under modular arithmetic ($\pmod n$), inspired by manual grid explorations (such as Mod 3 remainder tracking) and fractal geometry like the Sierpinski triangle.

## Overview
When you compute Pascal's triangle and apply the modulo operation at every step, the numbers repeat in mesmerizing geometric and algebraic patterns. 
* **Mod 2**: Forms the **Sierpinski Triangle** fractal.
* **Mod 3**: Forms nested self-similar triangular fractal patterns with three distinct remainder states ($0, 1, 2$).
* **General Mod $n$**: Reveals underlying number-theoretic properties connected to Lucas's Theorem and divisibility.

---

## Features
1. **General Modulo Engine**: Generate Pascal's triangle for any integer $n$.
2. **Remainder Mapping**: Color-code or symbol-map remainders (e.g., matching the $R:0, R:1, R:2$ color-coding from the notebook).
3. **Row Analysis**: Count and analyze the frequency of each remainder per row (extending the algebraic tracking of terms).
