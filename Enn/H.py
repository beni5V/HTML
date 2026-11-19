import sys
def countdown(num, depth, show):
    """ Return (no. of calls made, deeepest stack depth reached.) """
    if show:
        print(" " * depth + "countdown(" + str(num) + ") depth", depth)
    if num <= 0:
        return 1, depth
    calls, deepest = countdown(num - 1, depth + 1, show)
    return calls + 1, deepest

def countdown_loop(num):
    """The same countdown with a loop: no calls wait on the stack."""
    steps = 0
    while num > 0:
        steps = steps + 1
        num = num - 1
    return steps

start = int(input("Count down from which number? "))
print("Trace of countdown(" + str(start) + "):")
calls, deepest = countdown(start, 1, True)
print("calls =", calls, "  deepest depth =", deepest)
print()
print("     n | recursive calls | deepest depth | loop steps")
for n in range(0, 1001, 100):
    calls, deepest = countdown(n, 1, False)
    print(f"{n:>6} | {calls:>15} | {deepest:>13} | {countdown_loop(n):>10}")
print()
print("Python's limit on waiting calls here:", sys.getrecursionlimit())
try:
    calls, deepest = countdown(5000, 1, False)
    print("countdown(5000) finished:", calls, "calls")
except RecursionError:
    print("countdown(5000) -> RecursionError: the call stack is full")
print("countdown_loop(5000) ->", countdown_loop(5000), "steps (a loop needs no stack)")
