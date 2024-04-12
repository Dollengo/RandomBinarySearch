import random

def binary_search(list, first_index, last_index, searched_value):
    if last_index >= first_index:
        middle_element_index = (first_index + last_index) // 2
        middle_element = list[middle_element_index]
        
        if middle_element == searched_value:
            return f"{middle_element} found in position {middle_element_index + 1};"
        elif middle_element < searched_value:
            return binary_search(list, middle_element_index + 1, last_index, searched_value)
        else:
            return binary_search(list, first_index, middle_element_index - 1, searched_value)
    else:
        return f"{searched_value} not found."

attempts = 1
value_sought = input((int)"Value sought: ")
result = f"{value_sought} not found."

while result == f"{value_sought} not found.":
    ordered_vector = sorted([random.randint(0, 1000000000) for _ in range(10)])
    result = binary_search(ordered_vector, 0, len(ordered_vector) - 1, value_sought)
    print(result, "Attempts: ", attempts)
    attempts += 1
