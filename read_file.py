import os
from pypdf import PdfReader
import pandas as pd

def file_checker(file_path):
    if file_path.endswith('.pdf'):
        return 'pdf'
    elif file_path.endswith('.csv'):
        return 'csv'
    else:
        return 'txt'

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")

    else:
        file_type =  file_checker(file_path)
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
