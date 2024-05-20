#Creating a string variable
name= "python"
print(name)
message ='I love python'
print(message)

str1= 'Hello World'
str2= 'I love python'
str3= 'Hello World'
#compare str1 & str2
print(str1==str2)
#compare str2 & str3
print(str1==str3)

 #if...elif...else statement
grade = 83
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
    print('F')
#loop in python (for loop)
names = ['James', "Marion",'May', "Peter"]
for name in names:
    print(name)
#trial1forloop
subjects = ['Biology','Chemistry',"Physics","Computer studies"]
for subject in subjects:
    print(subject)
#range for loop
subjects = ['Biology','Chemistry',"Physics","Computer studies"]
for i in range(0,3,1):
    print(subjects)