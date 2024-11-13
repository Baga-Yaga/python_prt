import numpy as np
import pandas as pd

# Creating arrays using numpy
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating a DataFrame using pandas
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
})

# Displaying the arrays and DataFrame
print("1D Array:\n", arr_1d)
print("\n2D Array:\n", arr_2d)
print("\nDataFrame:\n", df)

# Basic arithmetic operations using numpy
print("\nAddition:\n", arr_1d + 10)
print("\nSubtraction:\n", arr_1d - 2)
print("\nMultiplication:\n", arr_1d * 3)
print("\nDivision:\n", arr_1d / 2)

# Basic arithmetic operations using pandas
print("\nDataFrame Addition:\n", df + 10)
print("\nDataFrame Subtraction:\n", df - 2)
print("\nDataFrame Multiplication:\n", df * 3)
print("\nDataFrame Division:\n", df / 2)

# Statistical operations using numpy
print("\nMean of 1D Array:", np.mean(arr_1d))
print("Mean of 2D Array (axis=0):", np.mean(arr_2d, axis=0))
print("Mean of 2D Array (axis=1):", np.mean(arr_2d, axis=1))

# Statistical operations using pandas
print("\nMean of DataFrame:\n", df.mean())
print("\nSum of DataFrame:\n", df.sum())
print("\nStandard Deviation of DataFrame:\n", df.std())

# Accessing elements using numpy
print("\nElement at index 2 of 1D Array:", arr_1d[2])
print("Element at row 1, column 2 of 2D Array:", arr_2d[1, 2])

# Accessing elements using pandas
print("\nElement at row 2, column 'B' of DataFrame:", df.loc[2, 'B'])
print("Element at row 3, column 'C' of DataFrame:", df.iloc[3, 2])

# Slicing arrays using numpy
print("\nSlicing 1D Array (indices 1 to 3):", arr_1d[1:4])
print("Slicing 2D Array (rows 1 to 2, columns 1 to 2):\n", arr_2d[1:3, 1:3])

# Slicing DataFrame using pandas
print("\nSlicing DataFrame (rows 1 to 3, columns 'A' and 'C'):\n", df.loc[1:3, ['A', 'C']])
print("Slicing DataFrame (rows 0 to 2, columns 0 to 1):\n", df.iloc[0:3, 0:2])

# Boolean indexing using numpy
print("\nElements greater than 3 in 1D Array:", arr_1d[arr_1d > 3])
print("Elements greater than 5 in 2D Array:\n", arr_2d[arr_2d > 5])

# Boolean indexing using pandas
print("\nRows where column 'A' is greater than 3:\n", df[df['A'] > 3])
print("Rows where column 'B' is less than 9:\n", df[df['B'] < 9])

# Reshaping arrays using numpy
reshaped_arr = arr_2d.reshape(1, 9)
print("\nReshaped 2D Array to 1D:\n", reshaped_arr)

# Transposing arrays using numpy
transposed_arr = arr_2d.T
print("\nTransposed 2D Array:\n", transposed_arr)

# Concatenating arrays using numpy
arr_concat = np.concatenate((arr_1d, arr_1d))
print("\nConcatenated 1D Arrays:\n", arr_concat)

# Concatenating DataFrames using pandas
df_concat = pd.concat([df, df], axis=1)
print("\nConcatenated DataFrames:\n", df_concat)

# Sorting arrays using numpy
sorted_arr = np.sort(arr_1d)
print("\nSorted 1D Array:\n", sorted_arr)

# Sorting DataFrame using pandas
df_sorted = df.sort_values(by='B', ascending=False)
print("\nSorted DataFrame by column 'B':\n", df_sorted)