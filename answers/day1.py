from io import TextIOBase
import string


def convert_str_to_number(text: str):
    digts = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    # pattern = re.compile("|".join(re.escape(k) for k in digts.keys()))
    # return pattern.sub(lambda x: digts[x.group()], line)
    for word, number in digts.items():
        text = text.replace(word, number)
    return text


def first_last_digit(line: str):
    numbers = [c for c in line if c in string.digits[1:]]
    return int(numbers[0] + numbers[-1])


def answer(input_file: TextIOBase):
    data = input_file.read().splitlines()

    part1 = sum([first_last_digit(line) for line in data])
    print(f"Day 1, part1 answer = {part1}")

    part2 = sum([first_last_digit(convert_str_to_number(line)) for line in data])
    print(f"Day 1, part2 answer = {part2}")
