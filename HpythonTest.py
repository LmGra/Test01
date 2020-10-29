#Clicker Test
import random
maxhp = 10
damage = round(random.random() * 10)
print ("Actualmente tienes "+ str(maxhp) + " de vida")
input()
#raw_input()
hp = maxhp - damage
print ("Has sufrido "+ str(damage) +" de daño, tienes " + str(hp) + " de vida restante")
if hp <= 0:
	print ("Has muerto")

#Añado texto al final para ver si se guarda el commit.