from sys import exit as sys_exit

from modules.card_class import Card


def exit_code_generator(__exit_reason: str, *__args) -> str:
    padding: str = " " * 50 + "\n"
    exit_code: str = padding + __exit_reason + "\n"

    for arg in __args:
        exit_code += padding + str(arg)

    exit_code += padding
    return exit_code


def sanitise_file_data(__file_data: list[str]) -> list[str]:
    sanitised_file_data: list[str] = []

    for line in __file_data:
        if line[0] != "#":
            sanitised_line: str = line.replace("\n", "")
            sanitised_file_data.append(sanitised_line)

    return sanitised_file_data


def convert_file_data_to_card_class(__file_data: list[str]) -> Card:
    card: Card = Card()

    for line in __file_data:
        key, value = line.split(":")
        value = value[1:]

        if key == "Filetype":
            card.set_file_type(value)

        elif key == "Version":
            card.set_file_type_version(value)

        elif key == "Device type":
            card.set_device_type(value)

        elif key == "UID":
            card.set_uid(value)

        elif key == "ST25TB Type":
            card.set_st25tb_data_type(value)

        elif key == "System OTP Block":
            card.set_system_otp_block(value)

        elif "Block " in key:
            card.add_block_to_matrix(value)

        else:
            exit_code: str = exit_code_generator("data_manipulator.py > cconvert_file_data_to_card_class > unmanaged data type", key, value)
            sys_exit(exit_code)

    return card