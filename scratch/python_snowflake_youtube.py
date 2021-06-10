# https://www.youtube.com/watch?v=0mfsY5ZWmMY


#input: a2z2b4
#output: aaazzzbbbbb

import re

def string_repeat(input):
    spl = re.findall("(\D+)(\d+)", input)
    result = ""
    for g in spl:
        result = result + str((g[0] * (int(g[1]) + 1)))
    return result

def string_repeat2(input):
    output_string = ""
    current_string = ""
    for i, j in enumerate(input):
        if j.isdigit():
            output_string += str(current_string) + str(current_string) * int(j)
            current_string = ""
        else:
            current_string += str(j)

    return output_string

input1 = "a2z2b4"
input2 = "a2z2b4car3"

print(string_repeat(input1))
print(string_repeat2(input1))

print(string_repeat(input2))
print(string_repeat2(input2))
