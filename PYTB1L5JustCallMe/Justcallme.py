import sys
import time

def CallMe(name, number):
	print("1-Hallo?")
	time.sleep(2)
	print("1-Wie is daar?")
	time.sleep(2)
	print("2-Ik ben het "+ name)
	time.sleep(2)
	print("1-Heeeyyy "+ name+ " ik bel je later even terug ja? ben erg druk")
	time.sleep(2)
	print("2-Tuurlijk! spreek je later dan")
	time.sleep(2)
	print("1-Wacht!!! wat is je nummer want anders kan ik je niet terug bellen")
	time.sleep(2)
	print("2-Ja is goed me nummer is "+ number)
	time.sleep(4)
	print("1-Okey top heb hem genoteerd, Spreek je later")
	time.sleep(2)
	print("2-Laterrrsss")
	print("Beep beep beep.....")

CallMe(sys.argv[1], sys.argv[2])