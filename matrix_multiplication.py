
job_name = "MatrixMultiplicationJob"
input_path = "/user/hadoop/matrix_input/"
output_path = "/user/hadoop/matrix_output/"
mapper_script = "mapper.py"
reducer_script = "reducer.py"
job_status = "RUNNING"

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

def mapper(A, B):
    mapped = []
    n = len(A)         
    m = len(A[0])      
    p = len(B[0])       

    for i in range(n):
        for j in range(p):
            for k in range(m):
                mapped.append(((i, j), A[i][k] * B[k][j]))
    return mapped

def reducer(mapped_data):
    reduced = {}
    for key, value in mapped_data:
        if key not in reduced:
            reduced[key] = 0
        reduced[key] += value
    return reduced

job_status = "MAPPER_RUNNING"
mapped_data = mapper(A, B)
job_status = "REDUCER_RUNNING"
reduced_data = reducer(mapped_data)
job_status = "COMPLETED"
n = len(A)
p = len(B[0])
result = [[0]*p for _ in range(n)]
for (i, j), val in reduced_data.items():
    result[i][j] = val
print("Matrix Multiplication Result:")
for row in result:
    print(" ".join(map(str, row)))
with open("matrix_result.txt", "w") as f:
    for row in result:
        f.write(" ".join(map(str, row)) + "\n")
