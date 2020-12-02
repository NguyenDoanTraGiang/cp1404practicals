import random


def main():
    score = float(input("Enter score: "))
    print(validate_score(score))

    print("\nRandom score's result:")
    random_number = random.randint(0, 100)
    print(validate_score(random_number))


def validate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
