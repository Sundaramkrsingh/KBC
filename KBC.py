questions=["Who is the founder of Chat-GPT?","What is the full form of CSS","Which was the first functional programming language?","The first month of indian national calendar is","Which platform is used to work on projects?","Which one of the following is essentially a solo dance?","Who is the current governer of RBI?","Who is our Finance Minister","When was Chandrayan-2 launched","What was the highest package bagged in year 2020","Which IIT is ranked first?","Which of these states has had the most number of its governors become presidentsof india?","Which of these scientists does not have a chemical element on the perioic table named after him?","The language of Lakshadweep is","September 27 is celebrated every year as","Ghatotkach in Mahabharata was son of","Which of the following is a folk dance of india"]


options=[["Sam Altman","Mark zukerberg","Elon Musk","Bill Gates"],["Cascading spread sheets","Central style studio","Cascading style sheets","Cascading style symbols"],["Swift","C++","ANSI-C","Java"],["Magha","Chaitra","Ashadha","Vaishakha"],["GitHub","Geeks For Geeks","Leet Code","Coding Ninjas","Go Daddy"],["Kuchipudi","Kathak","Manipuri","Mohiniattam"],["Amit Shah","Nirmala Sitaraman","ShaktiKanta Das","Arun Jateli"],["Amit Shah","Narendra Modi","Dr.JayShankar","Nirmala Sitaraman"],["23 june 2020","22 june 2019","12 May 2020","21 july 2019"],["1.8Cr","2Cr","4Cr","2.2Cr"],["IIT Mumbai","IIT Indore","IIT Roorkee","IIT Hyderabad"],["Rajasthan","Bihar","Punjab","Andhra pradesh"],["Albert Einstein","Alfed Nobel","Thomas Edison","Enrico Fermi"],["Tamil","Hindi","Malyalam","Telugu"],["Teachers' Day","International Literacy Day","National Integration Day","World Tourism Day"],["Duryodhana","Arjuna","Bhima","Yudhisthir"],["Kathakali","Mohiniattam","Garba","Manipuri"]]


correct_opt=['A','C','C','B','A','C','C','D','B','D','A','B','C','C','D','C','C']


prizes=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,'1Cr','7.5Cr']


while True:
    print("**              Welcome to KBC India             **\n\nEnter '1' to Start and '0' to exit")

    x=int(input())
    if x==0:
        break
    elif x!=0 and x!=1:
        raise ValueError("You have given an inavlid input\nPlease restart to play")
    else:
        i=0
        while i<len(questions):
            print(questions[i])
            print("\nA.",options[i][0],'       ',"B.",options[i][1],"\nC.",options[i][2],'       ',"D.",options[i][3])
            if i<4:
                money=0
            elif i>4:
                money=10000
            elif i>9:
                money=320000
            elif i>14:
                money=7500000
            else:
                money='7.5Cr'
            A=input("\nGive your answer: \n\n")
            if A==correct_opt[i]:
                print(f"Congrats! You have Won Rs:{prizes[i]}\n")
                i+=1
                continue
            if A not in correct_opt:
                raise ValueError("You have given an invalid input\nPlease restart for playing")
            if A!=correct_opt[i]:
                print(f"Nice Try, Your total winning amount is: {money}\nEnter '0' to exit (or) '1' to play again\n\n")
                break
            if i==16:
                break