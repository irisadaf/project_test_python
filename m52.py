# def natural_numbers():
#     n = 1
#     while True:  # Infinite loop
#         yield n  # Yield the current number
#         n += 1   # Increment the number
#
# # Using the generator
# if __name__ == '__main__':
#     number_generator = natural_numbers()  # Create a generator instance
#
#     for _ in range(10):  # Get the first 10 natural numbers
#         print(next(number_generator))  # Use next() to get the next value from the generator



def read_file_line_by_line(file_path):
    """Generator to read a file line by line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line without leading/trailing whitespace

if __name__ == '__main__':
    # Specify the path to your text file
    file_path = 'example.txt'  # Replace with your actual file path

    # Create the generator
    line_generator = read_file_line_by_line(file_path)

    # Process each line from the generator
    for line in line_generator:
        print(line)  # Print each line (you can process it as needed)