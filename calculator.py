import random
import time
MIN_TERM= 1
MAX_TERM= 8
OPERATOR= ["+","-","*"]
TOTAL_PROBLEM=10
def cal():

    num1 = random.randint(MIN_TERM,MAX_TERM)
    num2 = random.randint(MIN_TERM,MAX_TERM)
    operator= random.choice(OPERATOR)
    expr = str(num1) + "" + operator + "" + str(num2)
    answer = eval(expr)
    return  expr , answer  
    # print(expr)
    # print(num1 , operator,  num2 , answer)

count = 0
input("Press enter yo start!")
print("____________________")
start_time = time.time()
for i in range(TOTAL_PROBLEM):
        expr, answer = cal()
        # print(expr,answer)
        print(i)
        # print("Problem #" +" "+ str(i+1) + " "+str(expr) + "=" + str(answer) )
        while True:
            guess = input("problem #" + str(i+1) + " :"+ expr + "=")
            if guess == str(answer):
                break
            count += 1

end_time = time.time()
Total_time = round(end_time-start_time,2)

print("_______________________")
print("Nice work!!! you finished in time " , Total_time , "with wrong attemps" , count)


