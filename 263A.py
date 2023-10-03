'''
Attempt at implementing problem 263A at codeforces: A Beautiful Matrix:

You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.

'''

#Get the input matrix
def get_input() -> list:
    rows = []
    for i in range(5): #The input will be a 5 by 5 matrix.
        row = input()
        row = row.split(" ")
        rows.append(row)
    return rows

def find_one(input_matrix: list) -> list:
    rows = 5
    columns = 5
    for row in range(rows):
        for col in range(columns):
            if input_matrix[row][col] == "1":
                return [row, col]

def main() -> None:
    matrix = get_input()
    one_index = find_one(matrix)
    #To find the minimum moves, we subtract from each row and column component the row and column coordinate of the middle
    #of the matrix, which is (3,3)
    sum = abs(one_index[0]-2) + abs(one_index[1]-2) #We subtract 2, because (2,2) is the INDEX of the middle of the matrix.
    print(sum)

main()