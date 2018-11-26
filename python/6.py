print("Enter your marks:")
marks=input()
if(marks>=80 and marks<100):
    print("You will get A+")
elif(marks>=75 and marks<80):
    print("You will get A")
elif(marks>=70 and marks<75):
    print("You will get A-")
elif(marks>=65 and marks<70):
    print("You will get B+")
elif(marks>=60 and marks<65):
    print("You will get B")
elif(marks>=55 and marks<60):
    print("You will get B-")
elif(marks>=50 and marks<55):
    print("You will get C")
elif(marks>=40 and marks<50):
    print("You will get D")
else:
    print("You will fail in the Exam")
