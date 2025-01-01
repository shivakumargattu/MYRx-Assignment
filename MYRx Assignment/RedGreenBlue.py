#3 Given an array of Red Green Blue balls.You have to sort it. 

def sort_balls(balls):
    balls.sort(key=lambda x: {'B': 0, 'G': 1, 'R': 2}[x])
    return balls

input_balls = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sort_balls(input_balls))  # Output: ['B', 'B', 'B', 'G', 'G', 'G', 'G', 'R', 'R']

# another method is


input_balls.sort()
print(input_balls) # Output: ['B', 'B', 'B', 'G', 'G', 'G', 'G', 'R', 'R']