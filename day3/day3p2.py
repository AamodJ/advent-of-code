with open("input.txt", "r") as fd:
    banks = fd.readlines()
    banks = [bank.strip() for bank in banks]


output_joltage = 0
for bank in banks:
    bank_joltage = 0
    original_bank = bank
    for i in range(11, -1, -1):
        if i == 0:
            msd = max([int(battery) for battery in list(bank)])
            msd_idx = bank.index(str(msd))
        else:
            msd = max([int(battery) for battery in list(bank[:-i])])
            msd_idx = bank[:-i].index(str(msd))

        bank = bank[msd_idx + 1 :]

        bank_joltage = bank_joltage * 10 + msd

    output_joltage += bank_joltage
    print(f"Bank: {original_bank}. Max Possible Joltage: {bank_joltage} jolts")

print(f"Total output joltage: {output_joltage}")
