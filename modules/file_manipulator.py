from os import listdir


def get_directory_filenames(__directory_name: str) -> list[str]:
    return listdir(__directory_name)


def get_file_data(__filepath: str) -> list[str]:
    file_data: str = ""

    with open(__filepath, "r") as file:
        file_data = file.readlines()

    return file_data