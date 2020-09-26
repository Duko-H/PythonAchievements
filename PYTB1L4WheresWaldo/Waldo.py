import random

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]

random.shuffle(people)

print(people)

for index in range( len(people) ):
	print( people[ index ] )
	if ( people[ index ] == "Waldo" ):
		print("Waldo is op Stoel", index + 1)
		break
  	
