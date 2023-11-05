import html
import unicodedata

__all__ = ["string_functions"]


def camel_case(string_value: str):
    stripped_string = string_value.strip()
    title_string = stripped_string.title()
    no_space_string = title_string.replace(" ", "")
    strip_first_char = no_space_string[1:]

    return no_space_string[0].lower() + strip_first_char


def capitalise(string_value: str):
    return string_value.capitalize()


def deburr(string_value: str):
    slug = unicodedata.normalize('NFKD', string_value).encode('ascii', 'ignore')
    return slug.decode('utf-8')


def ends_with(string_value: str, char_check: str, offset=0):
    string_len = len(string_value)
    if offset <= 1:
        last_char = string_value[string_len - 1]
    else:
        last_char = string_value[string_len - offset]
    return last_char == char_check


def escape(special_char: str):
    return html.escape(special_char)


def replace(main_string: str, to_replace: str, replace_with: str):
    return main_string.replace(to_replace, replace_with)


def string_functions():
    camel_case_result = camel_case("Foo bAr Poo")
    print("Camel Case Result = ", camel_case_result)

    capitalise_result = capitalise("foo bAr Poo")
    print("Capitalise Result = ", capitalise_result)

    deburr_result = deburr("áéíñóúü")
    print("Deburr Result = ", deburr_result)

    ends_with_result = ends_with("power", "r")
    print("Ends With Result = ", ends_with_result)

    ends_with_offset_result = ends_with("power", "e", 2)
    print("Ends With Offset Result = ", ends_with_offset_result)

    escape_result = escape("1&2")
    print("Escape Result = ", escape_result)

    replace_result = replace("Hi Fred", "Fred", "Barney")
    print("Replace Result = ", replace_result)
