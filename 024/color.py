'''Script to play with color codes, using generators and the colored package'''
import random

from colored import fg, attr
from colored.colored import colored

DEFAULT_TEXT = 'hello world'
EXCLUDE_COLORS = ('0', )  # black
COLORED_COLOR_CODES = list(set(colored(0).paint.values()) -
                           set(EXCLUDE_COLORS))
assert '0' not in COLORED_COLOR_CODES


def gen_any_hex_color():
    while True:
        r, g, b = random.sample(range(0, 256), 3)
        yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()


def gen_colored_color():
    while True:
        color = None
        while not color or color in EXCLUDE_COLORS:
            color = random.choice(COLORED_COLOR_CODES)

        yield fg(color)


if __name__ == '__main__':
    a = gen_any_hex_color()
    c = gen_colored_color()

    reset = attr('reset')

    while True:
        answer = input(('\nOptions:\n'
                        '(a)ny hex color to copy to your web design\n'
                        '(c)olor text (= will ask for text, default option)\n'
                        '(q)uit\n\n'))

        if answer == 'q':
            print('Bye')
            break

        elif answer == 'a':
            color = next(a)
            print(color)

        elif answer == 'c' or not answer:
            text = input('Enter text (hit enter for default text): ')
            if not text:
                text = DEFAULT_TEXT

            color = next(c)
            print(color + text + reset)

        else:
            print('Invalid option, try again')
            continue
