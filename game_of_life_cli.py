'''
Attempt one: 29072022: Trying to come up with a naive approach to the problem
Rules to this solution:
1. For this attempt, we will not dwell deep into optimisation. 
2. I will use a sample list of list to build a matrix for the problem statement.
'''

matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]];

'''
Basic background: the output can be returned in a separate memory space or can be achieved by in-place operation. 
'''

#approach by utilising extra memory

def naive_solution(matrix):
    output_matrix = [[] for i in range(len(matrix))]

    m, n = len(matrix), len(matrix[0]);

    for i in range(m):
        for j in range(n):
              


print(naive_solution(matrix))