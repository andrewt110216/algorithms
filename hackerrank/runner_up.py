# Hackerrank Problem
# Find the runner-up score

# --- PROBLEM DESCRIPTION ---
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.

def find_runner_up(arr):
	sorted_arr = [arr[0]]
	for score in arr[1:]:
		for i in range(len(sorted_arr)+1):
			if i == len(sorted_arr):
				sorted_arr.append(score)
				break
			if score > sorted_arr[i]:
				sorted_arr.insert(i, score)
				break
	return sorted_arr[1]


# --- TEST CASES ---
print('--- Test Case 1: Expected Runner-up: 76')
result = find_runner_up([14, 95, 75, -52, -8, 76, -82])
print('  --- Runner-up: ', result)
assert result == 76
print('  --- Pass')

print('--- Test Case 2: Expected Runner-up: -5')
result = find_runner_up([1000, -500, -75, -200, -5, -12])
print('  --- Runner-up: ', result)
assert result == -5
print('  --- Pass')
