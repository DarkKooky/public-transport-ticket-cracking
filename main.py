from sys import exit as sys_exit

from modules.file_manipulator import get_directory_filenames, get_file_data

from modules.data_manipulator import exit_code_generator, sanitise_data
from modules.data_manipulator import convert_data_to_ticket, convert_hexes_to_decimals, convert_decimals_to_hexes
from modules.data_manipulator import find_ticket_data_differences, absolute_decimals_substractions

from modules.displayer import block_substraction_display

from modules.ticket_class import Ticket


def __before_and_after_use_block_substractions(__b_0_ticket: Ticket, __b_1_ticket: Ticket) -> None:
    ticket_b_data_differences: dict = find_ticket_data_differences(__b_0_ticket, __b_1_ticket)
    
    for key, value in ticket_b_data_differences.items():
        hex_b_0: list[str] = value[0].split(" ")
        hex_b_1: list[str] = value[1].split(" ")

        dec_b_0: list[int] = convert_hexes_to_decimals(hex_b_0)
        dec_b_1: list[int] = convert_hexes_to_decimals(hex_b_1)

        absolute_dec_diff: list[int] = absolute_decimals_substractions(dec_b_0, dec_b_1)
        absolute_hex_diff: list[str] = convert_decimals_to_hexes(absolute_dec_diff)

        block_substraction_display(key, str(hex_b_0), str(hex_b_1), str(dec_b_0), str(dec_b_1), str(absolute_dec_diff), str(absolute_hex_diff))
    return


def run() -> None:
    resource_directory_name: str = "resources"
    list_of_filepaths: list[str] = get_directory_filenames(resource_directory_name)

    tickets: dict = {}

    for filename in list_of_filepaths:
        filepath: str = resource_directory_name + "\\" + filename
        data: list[str] = get_file_data(filepath)
        sanitised_data: list[str] = sanitise_data(data)

        ticket: Ticket = convert_data_to_ticket(sanitised_data)
        tickets[filename]  = ticket

    if len(tickets) == 0:
        exit_code: str = exit_code_generator("main.py > run > no ticket in list")
        sys_exit(exit_code)

    b_0_filename = list(tickets.keys())[1]
    b_1_filename = list(tickets.keys())[2]

    __before_and_after_use_block_substractions(tickets[b_0_filename], tickets[b_1_filename])
    return


if __name__ == "__main__":
    run()