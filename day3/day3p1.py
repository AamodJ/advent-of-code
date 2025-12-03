with open("input.txt", "r") as fd:
    banks = fd.readlines()
    banks = [bank.strip() for bank in banks]

output_joltage = 0
for bank in banks:
    msd = max([int(battery) for battery in list(bank[:-1])])
    msd_idx = bank[:-1].index(str(msd))

    lsd = max([int(battery) for battery in list(bank[msd_idx + 1 :])])

    bank_joltage = msd * 10 + lsd

    output_joltage += bank_joltage
    print(f"Bank: {bank}. MSD: {msd} LSD: {lsd}. Joltage: {bank_joltage} jolts")

print(f"Total output joltage: {output_joltage}")
