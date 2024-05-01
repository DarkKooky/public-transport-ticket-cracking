from sys import exit as sys_exit
from modules.card_class import Card


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


def compare_card_data(__card_a: Card, __card_b: Card) -> dict:
    differences: dict = {}
    card_class_attributes: list[str] = [x for x  in __card_a.__dir__() if "_Card" in x]

    for attribute_name in card_class_attributes:
        attribute_a = __card_a.__getattribute__(attribute_name)
        attribute_b = __card_b.__getattribute__(attribute_name)
        
        attribute_a_type = type(attribute_a)

        if attribute_a_type == str:
            differences = __compare_strings(attribute_a, attribute_b, differences, attribute_name)

        elif attribute_a_type is list:
            differences = __compare_lists(attribute_a, attribute_b, differences, attribute_name)

        else:
            exit_code: str = "=" * 50 + "\n"
            exit_code += "Unmanaged attribute type comparison\n"
            exit_code += "=" * 50 + "\n"
            exit_code += "ATTRIBUTE TYPE\n"
            exit_code += str(attribute_a_type)  + "\n"
            exit_code += "=" * 50 + "\n"
            sys_exit(exit_code)

    return differences