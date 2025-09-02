# Write a script that:
# Reads the file.
# Extracts all lines starting with [ERROR].
# Stores them in a separate file errors.txt.
# Prints the number of errors found.

with open('/Users/rohith/rohith-data-engineer-prep/Week_01/ Python_Deep_Dive/Day_01/programs/raw_logs.txt') as f:
    for_data = f.read().split('\n')
    for log in for_data:
        if log.startswith('[ERROR]'):
            with open('/Users/rohith/rohith-data-engineer-prep/Week_01/ Python_Deep_Dive/Day_01/programs/formatted_logs.txt', 'a') as f:
                f.write(log)
                f.write('\n')

# File paths
# input_file = "/Users/rohith/rohith-data-engineer-prep/Week_01/Python_Deep_Dive/Day_01/programs/raw_logs.txt"
# output_file = "/Users/rohith/rohith-data-engineer-prep/Week_01/Python_Deep_Dive/Day_01/programs/errors.txt"

# # Read input file
# with open(input_file, "r") as f:
#     lines = f.readlines()

# # Filter lines starting with [ERROR]
# error_lines = [line for line in lines if line.startswith("[ERROR]")]

# # Write errors to a new file
# with open(output_file, "w") as f:
#     f.writelines(error_lines)

# # Print number of errors found
# print(f"Number of errors found: {len(error_lines)}")
