# Hackerrank Problem
# Lists

# --- PROBLEM DESCRIPTION ---
# Consider a list (list = []). You can perform the following commands:
#
#  - insert i e: Insert integer e at position i.
#  - print: Print the list.
#  - remove e: Delete the first occurrence of integer e.
#  - append e: Insert integer e at the end of the list.
#  - sort: Sort the list.
#  - pop: Pop the last element from the list.
#  - reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of
# commands where each command will be of the 7 types listed above. Iterate
# through each command in order and perform the corresponding operation on
# your list.

def lists(input_commands):
    lst = []
    commands = input_commands.split("\n")
    for command in commands:
        command = command.split()
        if command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
        else:
            print("BAD JOB! This command wasn't found. Move on to the next.")


# --- TEST CASES ---
print('--- Test Case 1. Expected Response: [12, 5, 0] ---')
i = "append 5\ninsert 6 0\nappend 12\nsort\nreverse\nprint"
lists(i)

print('--- Test Case 2. Expected Response: [6, 5, 10], [1, 5, 9, 10] ---')
i = "insert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\n"\
    "append 1\nsort\nprint"
lists(i)
