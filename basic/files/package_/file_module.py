def sum_file(a,b):
    result = a + b
    with open('sum.txt' , 'w+') as file:
        file.write(str(result))

def read_sum_file(filename='sum.txt'):
    with open(filename, 'r') as file:
        return int(file.read())

