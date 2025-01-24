 Day-24-LIS
Here's Python Program for LIS. Day 24 of Day 365.
Let's break down the basic steps for creating a Linear Independence Structure (LIS) in mathematics, particularly in the context of Linear Algebra.

 Steps to Determine Linear Independence
1. Define the Vectors: List out the vectors you need to check for linear independence. Let's call them \( \vec{v_1}, \vec{v_2}, \vec{v_3}, \dots, \vec{v_n} \).

2. Form a Matrix: Construct a matrix with these vectors as columns. For example, if you have three vectors in 3-dimensional space, your matrix \( A \) would be:
   \[
   A = \begin{pmatrix}
   \vec{v_1} & \vec{v_2} & \vec{v_3}
   \end{pmatrix}
   \]

3. Row Reduction: Use Gaussian Elimination (Row Reduction) to transform the matrix into Row Echelon Form (REF) or Reduced Row Echelon Form (RREF).
   - Swap rows, multiply rows by non-zero scalars, and add/subtract multiples of rows from each other to get as many leading 1s as possible.
   - This helps to see if there are any zero rows or if the pivot positions clearly show each vector contributes something new to the span.

4. Check Pivot Positions: Examine the pivot positions (leading 1s) in the REF/RREF.
   - If each column has a pivot position (none of the columns are zero columns), then the vectors are linearly independent.
   - If there are free variables or columns without pivot positions, then the vectors are linearly dependent.

 Example
Consider the vectors \( \vec{v_1} = (1, 0, 0), \vec{v_2} = (0, 1, 0), \vec{v_3} = (0, 0, 1) \).

1. Form the Matrix:
   \[
   A = \begin{pmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   \end{pmatrix}
   \]

2. Row Reduce: This matrix is already in RREF.
3. Check Pivot Positions: Each column has a leading 1. Thus, \( \vec{v_1}, \vec{v_2}, \vec{v_3} \) are linearly independent.

