#learning randomising the integers,etc 





import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
# if user_choice < 0 or user_choice > 2:
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")

# learning lists 
state_of_india =["Delhi","Uttar Pradesh","Lucknow","Bihar","Uttarakhand","Tamil Nadu","Kerala","Chandigarh","Chennai","Chattisgarh","Jammu & Kashmir","Manipur","Assam","Arunachal Pradesh"]

#for list
print (state_of_india [0])
print(state_of_india[1])
print(state_of_india[2])
print(state_of_india[-1])

state_of_india.append("Prakhar Singh Rana")
# append is used for adding anything to the string or list
#for checking append function
print(state_of_india)


import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# for randomising # for randomising we have to type first import random
#1 option
randomfd=random.choice(friends)
print(randomfd)

#2nd option
random_index=random.randint(0,1)
print(random_index)


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
num_of_states=len(states_of_america) #50>49
print(states_of_america[num_of_states-2])

#printing both frui veg together in list 
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
dirty_dozen=[fruits,veg]
print(dirty_dozen)



import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
# if user_choice < 0 or user_choice > 2:
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
