from sys import exit as sys_exit

from modules.ticket_class import Ticket


def exit_code_generator(__exit_reason: str, *__args) -> str:
    padding: str = " " * 50 + "\n"
    exit_code: str = padding + __exit_reason + "\n"

    for arg in __args:
        exit_code += padding + str(arg)

    exit_code += padding
    return exit_code


def sanitise_data(__data: list[str]) -> list[str]:
    sanitised_data: list[str] = []

    for line in __data:
        if line[0] != "#":
            sanitised_line: str = line.replace("\n", "")
            sanitised_data.append(sanitised_line)

    return sanitised_data


def convert_data_to_ticket(__data: list[str]) -> Ticket:
    ticket: Ticket = Ticket()

    for line in __data:
        key, value = line.split(":")
        value = value[1:]

        if key == "Filetype":
            ticket.set_file_type(value)

        elif key == "Version":
            ticket.set_file_type_version(value)

        elif key == "Device type":
            ticket.set_device_type(value)

        elif key == "UID":
            ticket.set_uid(value)

        elif key == "ST25TB Type":
            ticket.set_st25tb_data_type(value)

        elif key == "System OTP Block":
            ticket.set_system_otp_block(value)

        elif "Block " in key:
            ticket.add_block_to_matrix(value)

        else:
            exit_code: str = exit_code_generator("data_manipulator.py > convert_data_to_ticket > unmanaged data type", key, value)
            sys_exit(exit_code)

    return ticket


def __compare_strings(__string_a: str, __string_b: str, __differences: dict, __attribute_name: str) -> dict:
    differences: dict = __differences

    if __string_a != __string_b:
        differences[__attribute_name] = (__string_a, __string_b)

    return differences


def __compare_lists(__list_a: list, __list_b: list, __differences: dict, __attribute_name: str) -> dict:
    differences: dict = __differences

    len_a: int = len(__list_a)
    len_b: int = len(__list_b)
    list_range: int = len_a

    if len_a != len_b:
        differences[__attribute_name + "_length"] = (len_a, len_b)
        list_range = min(len_a, len_b)

    for i in range(list_range):
        differences = __compare_strings(__list_a[i], __list_b[i], differences, __attribute_name + "_" + str(i))

    return __differences


def compare_ticket_data(__ticket_a: Ticket, __ticket_b: Ticket) -> dict:
    differences: dict = {}
    ticket_class_attributes: list[str] = [x for x  in __ticket_a.__dir__() if "_Ticket" in x]

    for attribute_name in ticket_class_attributes:
        attribute_a = __ticket_a.__getattribute__(attribute_name)
        attribute_b = __ticket_b.__getattribute__(attribute_name)
        
        attribute_a_type = type(attribute_a)

        if attribute_a_type == str:
            differences = __compare_strings(attribute_a, attribute_b, differences, attribute_name)

        elif attribute_a_type is list:
            differences = __compare_lists(attribute_a, attribute_b, differences, attribute_name)

        else:
            exit_code: str = exit_code_generator("data_manipulator.py > compare_ticket_data > unmanaged attribute type comparison", attribute_a_type)
            sys_exit(exit_code)

    return differences


def convert_hexes_to_decimals(__hexes: list[str]) -> list[int]:
    decimals: list[int] = []

    for i in range(len(__hexes)):
        deecimal: int = int(__hexes[i], 16)
        decimals.append(deecimal)

    return decimals


def absolute_decimal_substraction(__decimals_0: list[int], __decimals_1: list[int]) -> list[int]:
    return [abs(__decimals_0[i] - __decimals_1[i]) for i in range(len(__decimals_0))]


def convert_decimals_to_hexes(__decimals: list[int]) -> list[str]:
    return [hex(decimal)[2:].upper() for decimal in __decimals]