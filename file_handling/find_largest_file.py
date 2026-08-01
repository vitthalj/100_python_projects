import os
from pathlib import Path
def find_largest_file(directory):
    """
    Find the largest file in the given directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search.
    Returns:
        tuple: A tuple containing the path to the largest file and its size in bytes.
    """
    largest_file = None
    largest_size = 0

    for file in Path(directory).rglob('*'):
        if file.is_file():
            size = file.stat().st_size
            if size > largest_size:
                largest_size = size
                largest_file = file
    return (largest_file, largest_size) if largest_file else (None, 0)

if __name__ == "__main__":
    directory = input("Enter the directory path to search for the largest file: ")
    largest_file, largest_size = find_largest_file(directory)
    if largest_file:
        print(f"The largest file is: {largest_file} with size {largest_size} bytes.")
    else:
        print("No files found in the specified directory.")