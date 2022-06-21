def binary_intervals(s):
    ones = []
    zeros = []

    for i in range(len(s)):
        start = i
        end = i
        if i + 1 < len(s) - 1:
            while s[end] == s[end + 1]:
                if end + 1 >= len(s) - 1:
                    end = len(s) - 1
                    break
                else:
                    end += 1
                    if end - start == 5:
                        break

            if end - start == 5:
                if s[start] == "1":
                    ones.append((start + 1, end + 1))
                else:
                    zeros.append((start + 1, end + 1))

    return zeros, ones


z, o = binary_intervals(input("Binary Number: "))

print(f"zeros: {z}")
print(f"ones: {o}")
