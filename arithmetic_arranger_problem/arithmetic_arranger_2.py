def arithmetic_arranger(arr, show_result = False):

    if len(arr) > 4:
        print("Error: To many problems.")
        return

    up_line = ''
    down_line = ''
    dividing_line = ''
    result_line = ''

    ops = {
      '-' : lambda x : str(x[0] - x[1]),
      '+' : lambda x : str(x[0] + x[1])
    }

    lines = None

    for items in arr:

        chunks = items.split()
        max_len = len(max(chunks))

        if not all([i.isnumeric() for i in chunks[::2]]):
            print("Error: Numbers must only contain digits.")
            return
        if chunks[1] not in ops.keys():
            print("Error: Operator must be '+' or '-'.")
            return
        if max_len > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

        line_len = max_len + 2
        up_line += chunks[0].rjust(line_len, ' ') + ' ' * 4
        down_line += chunks[1] + " " * (line_len - len(chunks[2]) - 1) + chunks[2] + ' ' * 4
        dividing_line += '-' * line_len + ' ' * 4

        if show_result:

            result = ops[chunks[1]]( [int(i) for i in chunks[::2]] )
            result_line += result.rjust(line_len, ' ') + ' ' * 4

    lines = '\n'.join([up_line, down_line, dividing_line])

    if show_result:
        lines += '\n' + result_line

    return lines

print(arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "123 + 49"], True))
