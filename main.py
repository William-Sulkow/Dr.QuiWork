import random
import time


def binary_intervals(s):
    ones = []
    zeros = []

    for i in range(len(s)):
        start = i
        end = i
        if i + 1 < len(s) - 1:
            if i == 0 or s[i] != s[i - 1]:
                while s[end] == s[end + 1]:
                    if end + 1 >= len(s) - 1:
                        end = len(s) - 1
                        break
                    else:
                        end += 1

                if s[start] == "1":
                    ones.append((start + 1, end + 1))
                else:
                    zeros.append((start + 1, end + 1))

    return zeros, ones


binary_string = ""
for _ in range(int(input("Length of binary string: "))):
    binary_string = binary_string + str(random.randint(0, 1))

start = time.time()
z, o = binary_intervals(binary_string)
end = time.time()

print(f"String: {binary_string}")
print(f"\nzeros: {z}")
print(f"ones: {o}")

print(f"\n\nExecuted in: {end-start} seconds.")