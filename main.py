from sys import exit as sys_exit

from modules.file_manipulator import get_directory_filenames, get_file_data
from modules.data_manipulator import exit_code_generator, sanitise_file_data, convert_file_data_to_card_class
from modules.data_analyser import compare_card_data

from modules.card_class import Card


def run() -> None:
    resource_directory_name: str = "resources"
    list_of_filepaths: list[str] = get_directory_filenames(resource_directory_name)

    list_of_cards: list[Card] = []

    for filename in list_of_filepaths:
        filepath: str = resource_directory_name + "\\" + filename
        file_data: list[str] = get_file_data(filepath)
        sanitised_file_data: list[str] = sanitise_file_data(file_data)

        card: Card = convert_file_data_to_card_class(sanitised_file_data)
        card.set_filename(filename)
        list_of_cards.append(card)

    if len(list_of_cards) == 0:
        exit_code: str = exit_code_generator("main.py > run > no card in list")
        sys_exit(exit_code)

    card_data_differences: dict = compare_card_data(list_of_cards[1], list_of_cards[2])
    
    for key, value in card_data_differences.items():
        print(key, "-", value)
        
    return


if __name__ == "__main__":
    run()