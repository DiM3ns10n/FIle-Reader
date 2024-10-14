import os
from pypdf import PdfReader
import pandas as pd

def file_checker(file_path):
    """
    Checks the file extension of the given file path and returns the type of file.

    Args:
        file_path (str): The path to the file to be checked.

    Returns:
        str: The type of file based on its extension. Returns 'pdf' for PDF files,
             'csv' for CSV files,'txt' for text files and 'unknown' all other file types.
    """
    if file_path.endswith('.pdf'):
        return 'pdf'
    elif file_path.endswith('.csv'):
        return 'csv'
    elif file_path.endswith('.txr'):
        return 'txt'
    else: 
        return 'unknown'

def read_file(file_path):
    """
    Reads a file and processes its content based on the file type.
    Parameters:
    file_path (str): The path to the file to be read.
    The function performs the following actions based on the file type:
    - If the file is a PDF, it prints the number of pages and allows the user to read a specific page.
    - If the file is a CSV, it reads the file into a pandas DataFrame and prints it.
    - For other file types, it reads and prints the file content as plain text.
    Note:
    - The function checks if the file exists before attempting to read it.
    - The function uses the `file_checker` function to determine the file type.
    - The function uses the `PdfReader` class to read PDF files.
    - The function uses the `pandas` library to read CSV files.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")

    else:
        file_type =  file_checker(file_path)
        if file_type == 'unknown':
            print("Unknown file type. Cannot read the file.")
        if file_type == 'pdf':
            reader = PdfReader(file_path)
            pages = len(reader.pages)
            print(f"Number of pages in {file_path} is {pages}")
            index = int(input("Enter the page number you want to read: "))
            index -= 1
            if index <= pages:
                print('\n' + reader.pages[index].extract_text())

        elif file_type == 'csv':
            df =  pd.read_csv(file_path)
            print(df)

        else:

            with open(file_path, 'r') as f:
                content =  f.read()
                print(content)

def main():
    file_path = input('Enter the file location:')
    try:
        read_file(file_path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
    #read_file('examples\pdf_example_1.pdf')
    #read_file('examples\csv_example.csv')
    #read_file('examples\text_example.txt')