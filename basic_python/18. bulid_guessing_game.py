
secret_word = "ant"
guess = ""
guess_count = 0
guess_limit = 2

while guess != secret_word and guess_count <= guess_limit:
    guess = input("enter a guess: ")
    guess_count += 1

if guess_count <= guess_limit:
    print("You Won")
else:
    print("You lost")