
#this algo shows how many times the number is modified until it reaches 0 within the context of the N3+1 math problem
number = 0
steps = 0



number = int(input("please enter a number:"))



while number > 1:
   if number % 2 == 0:
      number = number / 2
      #print(number)  #printing for testing
      steps = steps + 1
   else:  
        number = number * 3 + 1
        #print(number) #print for testing
        steps = steps + 1


print(steps)

