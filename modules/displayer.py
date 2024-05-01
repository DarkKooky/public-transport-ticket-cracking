def __separator() -> str:
    return "=" * 100


def __padding(__length: int) -> str:
    return " " * 39


def __base_10() -> str:
    return " --<base10>--> "


def __base_16() -> str:
    return " --<base16>--> "


def block_substraction_display(__operated_block: str, __hex_b_0: str, __hex_b_1: str,
                               __dec_b_0: str, __dec_b_1: str, __abs_dec_diff: str, __abs_hex_diff: str) -> None:
    print(__separator())
    print(__operated_block + "\n")
    print(__hex_b_0 + __base_10() + __dec_b_0)
    print(__hex_b_1 + __base_10() + __dec_b_1)
    print(__padding(39) + "<subtraction>")
    print(__padding(39) + str(__abs_dec_diff) + __base_16() + str(__abs_hex_diff))
    return