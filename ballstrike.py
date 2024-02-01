
import random

def generate_number():
    # while True:
        # try:
    num_digits = int(input("Enter the number of digits for the random number: "))
    if num_digits <= 0:
        raise ValueError("Number of digits must be greater than 0")
    # break
    else:
        num=['1','2','3','4','5','6','7','8','9']
        digits=random.sample(num, num_digits)
        
        print(digits)
        return digits, num_digits
    # print(len(digits))
                # for i, char in range()
                
# count = 10
# answer,length = generate_number()
# for _ in range(count):
#     userInput = input("Your count"+ str(count) +" as per number length" + str(length) + ": ")
#     # print(type(userInput))
#     count-=1
#     if len(userInput) !=length:
#         print("must be in number length: " + str(length))
#     else:
#         for i,char in enumerate(answer):
#             print(i,char)
#             # if answer[i]
#             if userInput[i] == answer[i] or userInput[i] == char:
#                 print(i)
                
            # print(answer[i])

# generate_number()
    

count = 10
answer, length = generate_number()

for _ in range(count):
    userInput = input("Your count " + str(count) + " as per number length " + str(length) + ": ")
    count -= 1

    if len(userInput) != length:
        print("Must be in number length: " + str(length))
    else:
        strikes = sum(user_digit == answer_digit for user_digit, answer_digit in zip(userInput, answer))
        balls = sum(user_digit in answer for user_digit in userInput) - strikes

        print("Strikes:", strikes)
        print("Balls:", balls + strikes)

