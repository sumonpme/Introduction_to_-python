#Students Grade Calculation project in python
Allmarks=("Enter Marks Obtained in all Subjects: \n")
markOne=int(input("Enter first marks:"))
markTwo=int(input("Enter second marks:"))
markThree=int(input("Enter third marks:"))
markFour=int(input("Enter fourth marks:"))
markFive=int(input("Enter fifth marks:"))
marksix=int(input("Enter sixth marks:"))             
tot =markOne+markTwo+markThree+markFour+markFive+marksix
avg= tot/6
    
if avg >=90 and avg <=100:
        print("Your Grade is A+")
elif avg>=80 and avg<=90:
        print("Your Grade is A")
elif avg >=70 and avg <=80:
         print("Your Grade is B")
elif avg>= 60 and avg <=70:
           print("Your Grade is C")
elif avg>= 50 and avg <=60:
           print("Your Grade is F")