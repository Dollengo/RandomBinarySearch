# **Script Explanation**:
# Import **Random** Module:
We start by importing the random module, which allows us to generate random numbers.

# Define **Binary Search** Function:
Here, we define a function called binary_search that implements the binary search algorithm. It takes four parameters: list, first_index, last_index, and searched_value.

# **Binary Search** Algorithm:
This algorithm is a method for finding a target value within a sorted array. It works by repeatedly dividing in half the portion of the list that could contain the target value until you've narrowed down the possible locations to just one.

# Main **Loop**:
The script initializes a variable attempts to track the number of attempts. It specifies the value to be searched (value_sought). Inside a while loop, it generates a sorted list of random numbers and performs a binary search to find the desired value. It prints the result of each attempt and increments the attempts counter until the value is found.

# Binary Search **Algorithm**:
Binary search is an efficient algorithm for finding a target value within a sorted array. Here's how it works:

# Initialize the **Search** Range:
Start with the entire sorted array. Set the first index (left pointer) to 0 and the last index (right pointer) to the length of the array minus 1.

# **Search** Process:

Calculate the middle index of the current range.
Compare the value at the middle index with the target value:
If they match, the search is successful.
If the middle value is smaller than the target, search the right half of the array.
If the middle value is greater than the target, search the left half of the array.
Repeat the process until the target value is found or the search range becomes empty.
# **Time** Complexity:

Binary search has a time complexity of O(log n), where n is the number of elements in the array. It's significantly faster than linear search (O(n)), especially for large arrays.
# **Important** Note:

Binary search requires the array to be sorted beforehand.
It's a divide-and-conquer algorithm that efficiently reduces the search space by half with each comparison.
This algorithm is commonly used in various applications, such as searching in databases, finding elements in sorted lists, and implementing efficient data structures like binary search trees.

**Fireship video explaining:** https://www.youtube.com/watch?v=MFhxShGxHWc
