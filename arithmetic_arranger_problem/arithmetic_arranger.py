"""
    Receives a list of strings that are arithmetic problems and 
    returns the problems arranged vertically and side-by-side. 
    If result is set to True, the answers are displayed as well.

    Possible errors:
        `Error: Too many problems.`: More than 5 problems supplied to the function.
        `Error: Operator must be '+' or '-'.`: The appropriate operators the function accepts are addition (+) and subtraction (-). 
                Multiplication and division will return an error. 
                Other operators not mentioned in this bullet point are not included.
        `Error: Numbers must only contain digits.`: Each number (operand) should only contain digits.
        `Error: Numbers cannot be more than four digits.`: Each operand (aka number on each side of the operator) has a max of four digits in width.
"""

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

def arithmetic_arranger(arr, show = False):
    if len(arr) > 5:
        return "Error: To many problems."

    up_line = ''
    down_line = ''
    dividing_line = ''
    result_line = ''

    lines = []

    for item in arr:

        up,down,arithmetic_split = set_lines(item)

        up_line += up + ' ' * 4
        down_line += down + ' ' * 4
        dividing_line += '-' * len(down) + ' ' * 4
        result_line += set_line_result(arithmetic_split, down)

    lines.append(up_line)
    lines.append(down_line)
    lines.append(dividing_line)
    lines.append(result_line)

    if show is False:
        for i in range(0,3):
            print(lines[i])
    else:
        for i in range(0,4):
            print(lines[i])

def set_lines(string):

    arr = string.split()
    up_len = None
    down_len = None

    if len(arr[0]) > len(arr[2]):
        up_len = 1
        down_len = len(arr[0]) - len(arr[2])
    else:
        up_len = (len(arr[2]) + 2) - len(arr[0])
        down_len = 1

    return ' ' * up_len + arr[0], arr[1] + ' ' * down_len + arr[2], arr

def set_line_result(arr, string):
    one,two = int(arr[0]), int(arr[2])

    options = {
      '-' : lambda x,y : x - y,
      '+' : lambda x,y : x + y
      }

    result = str(options.get(arr[1])(one,two))

    return (' ' * (len(string) - len(result))) + result + ' ' * 4

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])