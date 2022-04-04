print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age >= 45 and age <=55:
    print("It's free!")
  else:
    bill = 12
    print("Adult tickets are $12")
    
  photo = input("Do you want the photos? Y or N. ")
  if photo == "Y":
    #Add 3 dollar to their bills
    bill += 3
    
  print(f"The Total bill is ${bill}")
     
else:
  print("Sorry, you can't ride and buy ticket.")
