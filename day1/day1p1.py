pos = 50
passwd = 0

with open("input.txt", "r") as fd:
    for line in fd.readlines():
        dir = line[:1]
        mag = int(line[1:])

        if dir == "L":
            pos -= mag
        else:
            pos += mag

        pos = pos % 100
        if pos == 0:
            passwd += 1


print(f"Final position: {pos}. Password: {passwd}")
