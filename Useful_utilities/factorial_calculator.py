from functools import reduce

def calculate_factorial_for_loop(number):
    total = 1
    for prev_num in range(number, 0, -1):
        total *= prev_num
    return total
def calculate_factorial_reduce(number):
    return reduce(lambda x,y:  x*y, range(number,0,-1))

def calculate_posible_combinations(number_of_objects, max_sequance_size):
    return int(calculate_factorial_reduce(number_of_objects)/(calculate_factorial_reduce(max_sequance_size)*(calculate_factorial_reduce(number_of_objects-max_sequance_size))))

print(calculate_factorial_for_loop(5))
print(calculate_factorial_reduce(5))

print(calculate_posible_combinations(36, 10))