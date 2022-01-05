

def entryTime(s, keypad):

    # Function constraints
    if len(keypad) != 9:
        raise ValueError('length of keypad is not 9 !')
    if not keypad.isdigit():
        raise ValueError('keypad[i] do not Є [1-9]')
    if not (1 <= len(s) <= 10**5):
        raise ValueError('NOT: L ≤ |s| ≤ 105')

    keypad_index_ref = {
        0: [1, 3, 4],
        1: [0, 2, 3, 4, 5],
        2: [1, 4, 5],
        3: [0, 1, 4, 6],
        4: [0, 1, 2, 3, 5, 6, 7, 8],
        5: [2, 4, 7, 8],
        6: [3, 4, 7],
        7: [3, 4, 5, 6, 8],
        8: [4, 5, 7]
    }

    keypad_index = {}

    for key, value in keypad_index_ref.items():
        new_key = keypad[key]
        new_value = [keypad[i] for i in value]  # list comprehension
        # new_value = []
        # for i in value:
        #     new_value.append(i)
        keypad_index[new_key] = new_value

    output_time = 0
    for i in range(1, len(s)):
        value_ref = s[i-1]
        value = s[i]

        if value == value_ref:
            pass
        elif value in keypad_index[value_ref]:
            output_time += 1
        else:
            output_time += 2

    return output_time


if __name__ == '__main__':
    print(entryTime('423692', '923857614'))
