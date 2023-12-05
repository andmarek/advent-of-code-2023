from typing import DefaultDict

file_name = "test.txt"
with open(file_name, 'r') as f:
    data = f.read()
lines = data.split("\n")

def part_one():
    p1 = 0
    for i, line in enumerate(lines):
        card, rest = line.split(":")
        _id = int(card.split(" ")[-1])
        
        winners, mine = rest.split("|")

        winning_nums = [int(x) for x in winners.split()]
        my_nums = [int(x) for x in mine.split()]
        val = len(set(winning_nums) & set(my_nums))
        if val > 0: p1 += 2**(val-1)
    return p1


def part_two():
    card_counts = DefaultDict(int)
    for i, line in enumerate(lines):
        card_counts[i] += 1
        _, rest = line.split(":")
        
        winners_str, my_numbers_str = rest.split("|")

        winning_nums = [int(x) for x in winners_str.split()]
        my_nums = [int(x) for x in my_numbers_str.split()]

        matches = len(set(winning_nums) & set(my_nums))
        print(f"*** matches: {matches}")
        for j in range(matches):
            print(card_counts)
            card_counts[i+1+j] += card_counts[i]

    total_cards = sum(card_counts.values())
    return total_cards








print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")