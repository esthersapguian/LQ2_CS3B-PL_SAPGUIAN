"""

A. Run successfully your Q2 on code snippet via your Code Editor (VSCode)
B. Send a Screenshot of the source code and at least 2 rerun results
C. Refactor the source code on the following instructions:
Store the values of the student and the classmate in a Dictionary
Store the length of the studentName and classMate in a List
Create a Callable Function which will contain the IF...ELIF...ELSE condition of the Q2 Original Source Code, then create a CALL FUNCTION to call this function every rerun.
Reverse the sort() of the classNumbers List
Create a variable that asks for User Input: Name of the User. Then this value will be the parameter passed to quizTwo().
D. Save, then upload here the github link of your source code

"""

#instantiation of variables

studentName = "Lewis Fonsi"
studentAddress = "City of Candon, Ilocos Sur"
studentFavNum1 = 25
studentAge = 25
studentAllowance = float(500)
studAllowance = int(studentAllowance)


classmateName = "Andrea Andres"
classmateAddress = "City of Vigan, Ilocos Sur"
classmateFavNum1 = "18"
classmateAge = "21"
classmateAllowance = "700"
classmateAgeInt = int(classmateAge)
classmateFavInt = int(classmateFavNum1)
classmateAllowanceF =float(classmateAllowance)
classmateAllowanceInt = int(classmateAllowanceF)


# Create a dictionary to store student and classmate names
nameDict = {
    'student': 'Lewis Fonsi',
    'classmate': 'Andrea Andres'
}

# Create a list to store the lengths of the student and classmate names

nameLen = [len(classmateName),len(studentName)]

def quizTwo(userInput):
    if "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress:
     print(studentName.upper(), "is from", studentAddress)
     print(classmateName.lower(), " is from ", classmateAddress)
    
    elif "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress:
     sName_Split = ["Lewis","Fonsi"]
     cName_Split = ["Andrea","Andres"]
     print("One among",sName_Split[0], cName_Split[0], "lives in Ilocos Sur")
    
    else:
     print("None of the students live in Ilocos Sur")
     
    if nameLen[1] < nameLen[0]:
         print(f"{userInput}, {classmateName.lower()} has a longer name than {studentName.upper()} with {nameLen[0]} letter over {nameLen[1]} letters")
    else:
        print(studentName.upper(), "has a lesser name than", classmateName.lower() ,"with", nameLen[1] , "letters over", nameLen[0],"letters")

 
userInput = input("Enter name: ")
quizTwo(userInput)
    
classNumbers = [studentFavNum1,studentAge,studAllowance ]
classNumbers.append(classmateAgeInt) #append or add classmateAgeInt
classNumbers.append(classmateFavInt)
classNumbers.append(classmateAllowanceInt)

classNumbers.sort(reverse=True)

for x in classNumbers: #print out the value of classNumbers using for loop
    print("Class Number: ",x) 

