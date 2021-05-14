from pathvalidate import ValidationError, validate_filename

import os
from pathlib import Path

from utils import valid_helper


@valid_helper
def validate_output_order(text: str) -> int:
    try:
        output_order = int(text)
    except (TypeError, ValueError):
        return None
    if output_order < 1 or output_order > 3:
        return None
    return output_order

@valid_helper
def validate_top(text: str) -> int:
    try:
        top = int(text)
    except (TypeError, ValueError):
        return None
    if top < 1:
        return None
    return top

@valid_helper
def validate_path(text: str) -> str:
    try:
        base_path = Path(__file__).resolve().parent
        path = os.path.join(base_path, text)
        validate_filename(text)
        f = open(path)
        f.close()
    except ValidationError:
        print("Ошибка валидации имени файла.")
        return None
    except IOError:
        print("Не удалось открыть файл.\n"
        "Возможно, файл не найден или Ваш диск заполнен.")
        return None

    return text

t_1 = """
Введите число, соответствующее типу сортировки:
1 - в порядке уменьшения количества символов в слове;
2 - в порядке частоты встречания слова в тексте;
3 - в алфавитном порядке.
"""

t_2 = """
Введите число, соответствующее максимальному количеству выдаваемых слов.
Число обязано быть больше нуля.
"""

t_3 = "Введите корректное название файла.\n"
