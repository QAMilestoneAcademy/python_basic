import random

actual_num=random.randint(1,10)
guess_num=0


while guess_num!=actual_num or guess_num!="exit":
    guess_num = int(input('Guess a number from 1 to 10? or type "exit"'))