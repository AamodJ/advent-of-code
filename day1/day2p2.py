pos = 50
passwd = 0
step = 0

with open("input.txt", "r") as fd:
    for line in fd.readlines():
        dir = line[:1]
        mag = int(line[1:])

        for i in range(mag):
            if dir == "L":
                pos -= 1
            else:
                pos += 1

            pos = pos % 100
            if pos == 0:
                passwd += 1

        step += 1

print(f"Total Steps: {step}. Final position: {pos}, passwd: {passwd}")
