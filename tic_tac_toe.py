import random





spots = {1: "1", 2: "2", 3: "3",
         4: "4", 5: "5", 6: "6",
         7: "7", 8: "8", 9: "9"}

def display_board():
    for i in range(1, 10, 3):
        print(" | ".join(spots[j] for j in range(i, i + 3)))
        if i < 10:
            print("-" * 9)

def user_move(mark):
    move = int(input("Siz hansı xananı seçəcəksiniz? (1-9): "))
    while move not in range(1, 10) or spots[move] != str(move):
        move = int(input("Yanlış xana. Düzgün bir xana seçin (1-9): "))
    spots[move] = mark

def check_winner():
    for i in range(0, 9, 3):
        if spots[i+1] == spots[i+2] == spots[i+3]:
            return True
    for i in range(1, 4):
        if spots[i] == spots[i+3] == spots[i+6]:
            return True
    if spots[1] == spots[5] == spots[9] or spots[3] == spots[5] == spots[7]:
        return True
    return False

def check_tie():
    return all(val in ("X", "O") for val in spots.values())

def game():
    print("Oyun Paneli:")
    display_board()

    user_input = input("Seçiminizi daxil edin (X və ya O): ")
    while user_input not in ("X", "O"):
        user_input = input("Yanlış seçim. X və ya O daxil edin: ")

    for _ in range(5):
        print("Oyun Paneli:")
        display_board()

        user_move(user_input)

        if check_winner():
            print("Təbriklər! Qalib gəldiniz!")
            return
        elif check_tie():
            print("Oyun berabərədir.")
            return

        bot_choice = random.randint(1, 9)
        while spots[bot_choice] != str(bot_choice):
            bot_choice = random.randint(1, 9)
        spots[bot_choice] = "X" if user_input == "O" else "O"

        print("Botun hərəkəti:")
        print("Oyun Paneli:")
        display_board()

        if check_winner():
            print("Təəssüf ki, bot qalib gəldi.")
            return
        elif check_tie():
            print("Oyun berabərədir.")
            return

    print("Oyun tamamlandı. Qalib gəlmədi.")

game()
