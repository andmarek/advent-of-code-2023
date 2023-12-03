from typing import DefaultDict
def part_one():
    allowed_color_amounts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    file_name = "input.txt"

    with open(file_name, "r") as f:
        data = f.read()
        games = data.split("\n")
        game_color_counts = {}
        for index, game in enumerate(games, 1):
            game_color_counts[index] = {}
            is_game_valid = True

            game_rounds = game.split(":")[1].split(";")

            for game_round in game_rounds:
                draws = game_round.split(", ")

                for draw in draws:
                    amount, color = draw.strip().split(" ")
                    if color in allowed_color_amounts.keys():
                        allowed_amount = allowed_color_amounts.get(color)
                        if int(amount) > allowed_amount:
                            is_game_valid = False
            game_color_counts[index] = is_game_valid 

        count = 0
        for k, v in game_color_counts.items():
            if v:
                count+=k
        return count

def part_two():
    file_name = "input.txt"
    min_colors = {}
    with open(file_name, "r") as f:
        data = f.read()
        games = data.split("\n")

        for index, game in enumerate(games, 1):
            min_colors[index] = {}

            for game_round in game.split(":")[1].split(";"):
                for draw in game_round.split(", "):
                    amount, color = draw.strip().split(" ")
                    min_colors[index][color] = max(min_colors[index].get(color, 0), int(amount))

        total_power = 0
        for game_id, game in min_colors.items():
            power = 1
            for _, amount in game.items():
                power *= amount
            total_power += power  
    return total_power

print(part_one())           
print(part_two())
