# Maximum Subarray Sum

This program calculates the maximum sum of any subarray in a list of numbers.

## Code

The main code is in the function `sub_suma_max(arr)`, where `arr` is the list of numbers.

### Function `sub_suma_max(arr)`

This function takes a list of numbers and returns the maximum sum of any subarray in the list.

The function iterates over each element in the list (considered as the start of a subarray) and then iterates from that point to the end of the list, adding each element to the current subarray. If the sum of the current subarray is greater than the maximum sum found so far, the maximum sum is updated.

### Execution and Time Measurement

The program also measures the execution time of the function `sub_suma_max(arr)`. To do this, it uses the function `time.perf_counter()` before and after the execution of `sub_suma_max(arr)`, and calculates the difference.

## Usage Example

Here is an example of how to use this program with the list of numbers `[1, -2, 3, 4, -5, 6, -7, 8, 9, -10]`:

```python
import time

# We declare the list of numbers we are going to use
numbers = [1, -2, 3, 4, -5, 6, -7, 8, 9, -10]

start_time = time.perf_counter()
max_sum = sub_suma_max(numbers)

# We calculate the execution time as the difference between the current time and the start time
execution_time = time.perf_counter() - start_time

print(f"The maximum sum of the subarray of the list: {numbers} is: {sub_suma_max(numbers)}.")
print(f"The execution time was: {execution_time} seconds.")
