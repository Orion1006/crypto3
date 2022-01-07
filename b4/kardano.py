import numpy as np
abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

grid_kardano = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
]

REPLACES = {
    ",": "ЗПТ",
    ".": "ТЧК",
    "-": "ТИРЕ",
    ";": "ТЧКИЗПТ",
}

def random_char(abc=abc):
    from random import choice

    return choice(abc)

def clear_text(text, abc=abc):
    import re

    text = replace_special(text, abc)
    text = text.lower()
    text = re.sub(f"[^{abc}]", "", text)
    return "".join([symbol for symbol in text.lower() if symbol in abc])

def replace_special(text, abc=abc, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text

def paste_values(text, template_grid, grid, abc=abc):
    indexes = np.argwhere(template_grid == 1)

    for row, col in indexes:
        if grid[row][col] != " ":
            raise ValueError("Введите другую решетку")
        grid[row][col] = text[0] if len(text) > 0 else random_char(abc)
        text = text[1:]
    return grid, text


def get_templates(grid):
    templates = [
        grid,
        np.rot90(grid, 2),
        np.flip(grid, axis=0),
        np.rot90(np.flip(grid, axis=0), 2),
    ]
    return templates


def fill_grid(text, template_grid, grid, abc=abc):

    for template in get_templates(template_grid):
        grid, text = paste_values(text, template, grid, abc)

    return grid


def enc(text, abc=abc, template_grid=grid_kardano, **kwargs):
    size = len(template_grid) * len(template_grid[0])

    assert (
        np.count_nonzero(template_grid) == size // 4
    ), "Количество ячейк должно = (строк*столбцов)/4"

    text = clear_text(text, abc)

    return ",".join(enc_block(text[i : i + size]) for i in range(0, len(text), size))


def enc_block(text, abc=abc, template_grid=grid_kardano, **kwargs):
    text = clear_text(text, abc)
    template_grid = np.array(template_grid)

    result = np.full(template_grid.shape, " ")

    result = fill_grid(text, template_grid, result, abc)
    result = " ".join(["".join(row) for row in result])

    return result


def get_text(grid, template_grid):
    indexes = np.argwhere(template_grid == 1)
    text = ""
    for row, col in indexes:
        text += grid[row][col]
    return text


def dec(grids, abc=abc, template_grid=grid_kardano, **kwarg):
    grids = grids.split(",")
    return "".join(dec_block(grid, abc, template_grid) for grid in grids)


def dec_block(grid, abc=abc, template_grid=grid_kardano, **kwargs):
    grid = [list(row) for row in grid.split()]
    template_grid = np.array(template_grid)

    result = ""
    for template in get_templates(template_grid):
        result += get_text(grid, template)

    return result

def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            print(enc(input("Введите сообщение: "))) 
        elif cmd == "2":
            print(dec(input("Введите сообщение: "))) 
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()