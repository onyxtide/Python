#Putting it all together by creating a sorting hat test with results
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("It's time to place you, little wizard, into a proper house for you! ")
print("A wizard should be laconic!")
print("This means that you should only use whole numbers to respond to the questions")
print("LET'S START!")

Q1 = int(input("Question number one: do you like 1)Dawn or 2)Dusk? "))

if Q1 == 1:
  Gryffindor += 1; Ravenclaw += 1
elif Q1 == 2: 
     Hufflepuff += 1;  Slytherin += 1
else: 
     print ("Wrong input, please use numbers only!") 
  
