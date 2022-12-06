

def read_txt_file(txt_file: str) -> str:
    """
    This function reads the txt file and prints the contents of the files
    :param txt_file:
    :return:
    """
    try:
        with open(txt_file, 'r') as fr:
            content = fr.readlines()
            return content
    except OSError as e:
        print(f'not found the file. '
              f'Error: {e}')
        return
    except Exception as e:
        print(f'unexpected error: -> {e}')
        return


if __name__ == '__main__':