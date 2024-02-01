
import random

def generate_number():
    while True:
        # try:
            num_digits = int(input("Enter the number of digits for the random number: "))
    #         if num_digits <= 0:
    #             raise ValueError("Number of digits must be greater than 0")
    #         break
        # except ValueError:
    #         print("Invalid input. Please enter a positive integer.")

    # # Generate the random number with unique digits
            num=['1','2','3','4','5','6','7','8','9']
            digits="".join(random.sample(num, num_digits))

            print("Generated random number:", digits)
generate_number()
