file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read()
lines = data.split("\n")

def part_one():
    total_points = 0

    for line in lines:
        matches = []
        card_points = 0

        card_part, rest = line.split(":")

        card_no = card_part.split(" ")[-1]
        winners, mine = rest.strip().split("|")

        winning_set = set([winner.strip() for winner in winners.strip().split(" ") if winner != ''])
        print(winning_set)
        for number in mine.strip().split(" "):
            if number in winning_set:
                if len(matches) >= 1:
                    card_points *= 2
                else:
                    card_points += 1
                matches.append(number)

        print(card_points)
        total_points += card_points
            

        # print(f"|{winners}|")
        
    return total_points


def part_two():
    pass

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")