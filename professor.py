import random

def main():
    level = get_level()
    score = 0
    problems_generated = 0

    while problems_generated < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
        problem_solved = False

        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    problem_solved = True
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if not problem_solved:
            print(f"{x} + {y} = {correct_answer}")

        problems_generated += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main() 