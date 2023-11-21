def fizzbuzz():
    while True:
      i = input("Enter the number: ")
      if i.isdigit():
         i = int(i)
         if i%3 == 0 and i%5 == 0:
             print("Buzzfizz")

         elif i%3 == 0 and i%5 != 0:
             print("Fizz")

         elif i%3 !=0 and i%5 == 0:
             print("Buzz")

         else:
             i%3 !=0 and i%5 !=0
             print(i)

      else:
         print("Enter valid input")



fizz=fizzbuzz()
print(fizz)