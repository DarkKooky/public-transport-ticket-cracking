from os import listdir


def get_filepaths_from_resource_directory(__resource_directory_name: str) -> list[str]:
    return listdir("resources")


def get_file_data(__filepath: str) -> list[str]:
    file_data: str = ""

    with open(__filepath, "r") as file:
        file_data = file.readlines()

    return file_data