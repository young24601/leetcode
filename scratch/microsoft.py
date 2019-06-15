# 60 minute time limit:
#
# a) recursively reverse a string.
#
# b) print a number vertically with each digit on its own line, without converting to a string.
# eg. 12345 becomes:
# 1
# 2
# 3
# 4
# 5
# (note you can do this problem just fine without needing a list or recursive stack...)
#
# c) remove all prime numbers from a linked list. (no mention of how large numbers could be)
import math

def part_a(inp: str) -> str:
    if len(inp) <= 1:
        return inp
    return inp[-1] + part_a(inp[0:-1])


def part_b(inp: int):
    divisor = 10 ** int(math.log10(abs(inp)))
    while divisor > 0:
        print(inp//divisor)
        # print(inp, "-", divisor * (inp//divisor))
        inp = inp - divisor * (inp//divisor)
        divisor = divisor//10




    #while divisor > 0:



print(part_a("abcdef"))
part_b(-12345)
