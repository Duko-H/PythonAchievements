import time

print("Hello I have some questions for you ")
print("What do you like more? Potato, Cheese, Salad. (Don't forget the capitals in your answers) ")

ans = input()

if ans == 'Potato':
	print("Your probably basic and neutral i like it!")

elif ans == 'Cheese':
	print("Your probably Dutch aren't you.")
elif ans == 'Salad':
	print("Your vegetarian....")

time.sleep(2)

print("Next question, What is the best drink in your opinion")
print("Cola, Fanta, Casis. (Don't forget your capitals!) ")

anss = input()

if anss == 'Cola':
	print("I like that one to.")

elif anss == 'Fanta':
	print("You are very fresh.")
elif anss == 'Casis':
	print("Your weird....")

print("Another question? Ja/Nee ")
quest = input()

if quest == 'Ja':
	print("What is your favorite genre out of these?")
	print("Horror, Action, Comedy. (Don't forget your capitals!")
ansss = input()

if ansss == 'Horror':
	print("Your emotionless...")

elif ansss == 'Action':
	print("You are kinda casual.")
elif ansss == 'Comedy':
	print("You are depressed when you are alone.")

elif quest == 'Nee':
	print("Alright bye!")

print("We shall meet again.")
quit()
        