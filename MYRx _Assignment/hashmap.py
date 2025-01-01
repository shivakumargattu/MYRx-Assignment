#5. Sort hashmap by value. 

# Input: Map: {101=John Doe, 102=Jane Smith, 103=Peter Johnson} 
# output: Map: {102=Jane Smith, 101=John Doe, 103=Peter Johnson}

def sort_hashmap(input_map):
    return dict(sorted(input_map.items(), key=lambda item: item[1]))

input_map = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
result=sort_hashmap(input_map)
print(result)  # Output: {102: 'Jane Smith', 101: 'John Doe', 103: 'Peter Johnson'}
