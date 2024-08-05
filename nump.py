import numpy as np
numstudents=int(input("Students: "))
numsubjects=int(input("Subjects: "))
marks=np.zeros((numstudents,numsubjects))


for i in range(0, numstudents):
    for j in range(0, numsubjects):
        marks[i,j]=int(input("Enter the grade:"))
        
print(marks)
        

S=np.sum(marks, axis=1)
print(S)    
percentage=(S/ (numsubjects * 100)) * 100 
print(percentage)   
    
for i in range(numstudents):
    if percentage[i]>=90:
        print("Student",i+1,":A+")
    elif percentage[i]>=80:
        print("Student",i+1,":A")
    elif percentage[i]>=70: 
        print("Student",i+1,":B+")
    elif percentage[i]>=60: 
        print("Student",i+1,":B")            
    elif percentage[i]>=50:
        print("Student",i+1,":C")
    else:
        print("Student",i+1,":F")
        
            
        
         
         
                