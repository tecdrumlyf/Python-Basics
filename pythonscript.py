#These functions below finds and imports the packages we need.
import pandas as pd
import os

#What directory are we getting the file from and reading the csv file.
Bob = os.getcwd()
Rob=os.path.join(Bob,'Downloads\\MOCK_DATA.csv') 
Jen = pd.read_csv(Rob) 

#Empty list for my for loops
templist = []
Bob =[]

for typethis in range(len(Jen)):  #Give the range/length of Jen.
    if typethis <= 8:  #if the counter is less than or equal to 8.
        print(Jen['email'][typethis]) #print out Jen's email list.
        templist.append(Jen['email'][typethis]) #add all above to the list (Jen).
    elif typethis <= 8:  #If counter(typethis) less than or equal to 8.
        Bob.append(Jen['email'][typethis]) #whatever the results above add them to bob's list.

for typethis in range(len(Jen)):
    if typethis <= 8: 
        print(Jen['email'][typethis])
        templist.append(Jen['email'][typethis])
    if typethis <= 8:
        Bob.append(Jen['ip_address'][typethis])  #add results from above"ip addresses"to Jen's list
        print(Jen['ip_address'][typethis])       #then print out the results of the whole list.

#break and continued statements
for i in range(len(Jen)):
    if i == 5 :  #example of boolean true or false
        break    
    print("broken loop") #anything under "if" is in one statement but anything tabbed out is a new statement

for typethis in range(len(Jen)):
    if Jen['ip_address'][typethis].isnull() == True: # .isnull doesn't work for strings, use instead np.where
        continue  #continue says if a certain condition is met ignore it and continue the loop.

i = 0  #set to zero to start the count at 0.
while i < 10:
    print(Jen['gender'][i]) #basically print to the gender column
    i = i + 1 #stops the counter from going on and on by setting it equal to it's self

i = 0
while i < 10:
#     print(i)
    if (Jen['gender'][i]) == 'Female': #becareful of capitailization of words/spelling
        #print(i)
        print(Jen['gender'][i])
    i = i  + 1  #don't leave this statement under print,it won't allow code to run 10#'s, cause it will get stuck when it's not female.