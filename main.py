from modules.file_manager import get_filepaths_from_resource_directory, get_file_data
from modules.data_manipulator import sanitise_file_data, convert_file_data_to_card_class
from modules.data_analyser import compare_card_data
from modules.card_class import Card


def run():
    resource_directory_name: str = "resources"
    list_of_filepaths: list[str] = get_filepaths_from_resource_directory(resource_directory_name)

    list_of_cards: list[Card] = []

    for filename in list_of_filepaths:
        filepath: str = resource_directory_name + "\\" + filename
        file_data: list[str] = get_file_data(filepath)
        sanitised_file_data: list[str] = sanitise_file_data(file_data)
        card: Card = convert_file_data_to_card_class(sanitised_file_data)
        card.set_filename(filename)
        list_of_cards.append(card)

    card_data_differences: dict = compare_card_data(list_of_cards[1], list_of_cards[2])
    
    for key, value in card_data_differences.items():
        print(key, "-", value)
        


if __name__ == "__main__":
    run()