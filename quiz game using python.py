#quiz game using python:
player=input("DO YOU WANT TO PLAY:")
a="yes"
if player==a:
    print("lets play")
else :
    print("bye")
score=0
Question_1=input("How Many Days Do we have in a week?")
if Question_1=="seven" :
    print("correct answer")
    score+=1
else:
    print("wrong answer")
Question_2=input("How Many players are their in cricket team?")
if Question_2=="eleven" :
    print("correct answer")
    score+=1
else:
    print("wrong answer")
Question_3=input("How Many districts are their in tamil nadu?")
if Question_3=="thirty nine" :
    print("correct answer")
    score+=1
else:
    print("wrong answer")
Question_4=input("How Many months are their in the year?")
if Question_4=="twelve" :
    print("correct answer")
    score+=1
else:
    print("wrong answer")
Question_5=int(input("How Many hours are their in the day?"))
if Question_5==24 :
    print("correct answer")
    score+=1
else:
    print("wrong answer")
print ("your score is:"+str(score))
