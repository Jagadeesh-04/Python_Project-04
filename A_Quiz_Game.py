# Project 4
# Project name : Quiz Competition generator !     
# After finishing the game the results will automatically sends to the users mail id .
# To send mail you have to import smtplib on your program ! and the json used to perform the json operations !
import smtplib
import json
x = 1
# Enter the answers for your questions in dictionary format 
answers = {1:'c',2:'d',3:'c',4:'a',5:'b',6:'d',7:'b',8:'a',9:'d',10:'a'}
score = 0
print("\nWelcome to the quiz competition ")
# To send the scores thorugh the email , you need the users mail id !
while x==1:
    mail = input("Enter #_Users mail id :") 
    print("Your mail id is :",mail)
    check = int(input("Is that Your mail id is correct ? \nIf Yes press : '0' \nIf No press : '1' \nYour response : "))
    if check==0:
        x+=1
    else:
        x+=0
# Open your json file which contains questions !
file = open("#json_file which includes questions !")
questions = json.load(file)
# After loading let users to attend the chellenge 
c= 1
print("\nYou are going to attend 10 MCQ \n\nThe Result will be published through your mail id !")
print( "\nYou have to mention the options only for the answers like ,\na\nb\nc\nd\nMake sure your options are with in the limit of 'a' to 'd'.\n \nLet's start !\n" )
for i in questions:
    print("Question no.",c)
    for j in questions[i]:
        print(j,":",questions[i][j])
    b = input("\nEnter the answer (option only) :")
    if b == answers[c] :
        if c == 10:
            print("Correct answer ! \nThanks for Attending our quiz chellenge ")
            break
        else:
            print("Correct answer \nnow move to the next one..!\n")
        score+=1
    else:
        print("wrong answer \nLet's try another one\n")
    c+=1
# Now we are going to send the Results to user's mail id
# 1st Create a connection
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#Enter the sender's mail id and password
server.login('#_Your_Mail_ID','#_Your_Mail_ID_Password') 
Result =f"SUBJECT : QUIZ COMPETITION RESULT\n\nWe Appriciate the time that you spended on our test \n\nHere Your Score is {score} out of 10"
#Assign Receivers mail id here ,
server.sendmail('#_Your_Mail_ID',mail,Result)
# Don't Forgot to quit the server !
server.quit
print("The Results are sended to your mail id ")