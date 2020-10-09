# ######Part 1 - without difficulty#######
# import random
# #Default health of a person
# health=50
#
# #Health pottion magically generates health
# health_potion=random.randint(25,50)
#
# #Once person drinks magic potion, his health gets changed
# health= health + health_potion
#
# print(health)

# #######Part 2 - with difficulty levels -1,2,3#######
#
import random
#Default health of a person
health=50
#
# #1,2,3 difficulty level of game
# #Higher the difficulty -lesser the potion
#
difficulty=3
#
# #Health potion magically generates health
health_potion=random.randint(25,50)/difficulty
#
# #Once person drinks magic potion, his health gets changed
health= health + health_potion

print(health)
#
