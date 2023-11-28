from enum import Enum


def extract_enums_list(enum_class) -> list[str]:
    return [member.value for member in enum_class]

