from sys import exit as sys_exit

from modules.file_manipulator import get_directory_filenames, get_file_data
from modules.data_manipulator import exit_code_generator, sanitise_data, convert_data_to_ticket, compare_ticket_data

from modules.ticket_class import Ticket


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

    ticket_b_with_cred = tickets[list(tickets.keys())[1]]
    ticket_b_without_cred = tickets[list(tickets.keys())[2]]

    ticket_b_data_differences: dict = compare_ticket_data(ticket_b_with_cred, ticket_b_without_cred)
    
    for key, value in ticket_b_data_differences.items():
        print(key, "-", value)
        
    return


if __name__ == "__main__":
    run()