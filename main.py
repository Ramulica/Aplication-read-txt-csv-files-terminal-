import sys
import csv
import os


def file_extension(file: str) -> str:
    """
    This function returns the file type if it's txt or csv
    if the file type is not rxt or csv it will return an empty string
    :param file:
    :return: file extension/empty string
    """


def read_txt_file(txt_file: str) -> str:
    """
    This function reads the txt file and prints the contents of the files
    :param txt_file:
    """


def read_csv_file(csv_file: str):
    """
    This function reads the csv file and prints the contents of the files
    :param csv_file:
    """


os.chdir("file_folder")
for item in sys.orig_argv[1::]:
    try:
        if file_extension(item) == "txt":
            read_txt_file(item)
            print("")

        elif file_extension(item) == "csv":
            read_csv_file(item)
            print("")
        else:
            print(f"{item} is neither txt nor csv\n")
    except  # complete with error and what happens if error occurs
