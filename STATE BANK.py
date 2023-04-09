print("===============================================")


customerNames=['poojitha', 'varsha','vijaya','akki','devu']  #this is i first i is 0 when new customer enters here
customerPins=['0523','0524','0525','0526','0527']
customerBalances=[10000,20000,30000,40000,50000]
deposition= 0
withdrawl= 0
balance= 0
counter_1= 1
counter_2= 5 #5 members in our bank
i= 0

while True:

    #this statement helps the program to run continously
    #os.system("cls")
    print("===================================================")
    print("******Welocme to STATEBANK OF INDIA**********")
    print("*************************************************")
    print("<<1.---- Open an New Account---->>>>")
    print("<<2.---- Withdrawl Money---->>>>")
    print("<<3.---- Deposit Money---->>>>")
    print("<<4.---- Check Customers and & Baalance---->>>>")
    print("<<5.---- Exit/quit---->>>>")

   #the below statement takes the choice number from the user
    choiceNumber=input("select a Choice number from the above options = ")

    if choiceNumber== "1":
        print("choice number 1 is selected by the customer")
        #the line below will take the no.of customers from the bank
        NOC=eval(input("Number of Customers")) #NOC=Number of customers
        i=i + NOC
          #523

        #The i condition will restrict the number of new accounts
        if i > 5: #output shows ("Customer registration exceed reached or customer registration too low") if usres more than 5 for new accounts
            print("\n")
            print("Customer registration exceed reached or customer registration too low")
            i=i - NOC
        else:
            #the while loop will run accoding to the customers
            while counter_1 <= i:
                #these few lines will take the information from customers

                name=input("Input Fullname:")
                customerNames.append(name) #it will append the new names of customers
                pin=str(input("Please chhose a valid pin"))
                customerPins.append(pin) #it will store and append the pin of new user
                balance=0
                deposition=eval(input("please input a value to deposit the money"))
                balance=balance+deposition
                customerBalances.append(balance)
                print("\nName=",end=" ")
                print(customerNames[counter_2])
                print("pin", end=" ")
                print(customerPins[counter_2])
                print("Balance", end=" ")
                print(customerBalances[counter_2],end=" ")
                print("/Rs")
                counter_1=counter_1 + 1 #new user added after created
                counter_2=counter_2 + 1  #after new pin new user added
                print("\n your name is added in the customer system")
                print(" your pin is added in the customer system")
                print("your balance is added in the customer system")
                print(" --- New account created successfully ----")

                print("\n") #next line
                print("y0ur name is available in the customers list")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name & Pin for Future")
                print("===============================================")
                #this statement below helps the user to go back to the start

        mainMenu=input("please press enter key to go back to Mainmenu")
    elif choiceNumber== "2":
       
       
        j = 0
        print("choice number 2 is selected by the customer")
        #this while loop will prevent the userr for using the account
        while j < 1: #Here 1 means counter_1 counter_1 has 5 members already fixed
            k = -1
            name=input("please input name:")
            pin=input("please input Pin:")

            #this while loop will keep the function running
            #customerNames List
            while k < len(customerNames) -1:
    
                k= k + 1
                #this two conditions find where both the names are in Customernames
                if name==customerNames[k]: #i have give some input names and pins already in customerNames 
                    if pin==customerPins[k]:
                        j= j + 1
                        #this staement would show the balance
                        print("Your current Balance", end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs\n")
                        balance=(customerBalances[k])

                        #statement below take the amount to withdraw from user
                        withdrawl=eval(input("Input value to withdraw: "))

                        #the if condition below would look whether withdrawl is graeate than bank amount if the user has 500 in bank and he withdraws 1000 then is incorrect

                        if withdrawl > balance:
                            deposition=eval(input("Please Deposit the Amount in Bank for suitable transaction"))
                            balance= balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance,end=" ")
                            print("-/Rs\n")
                            balance= balance - withdrawl
                            print("-\n")
                            print("-------Withdrawl successful-----------")
                            '''
                            speak="Thank you for crediting Money your available balance",print(balance)
                            text_speech.say(speak)
                            text_speech.runAndWait() '''

                            customerBalances[k]= balance  #523
                            
                            print("Your New Balance:",balance,end=" ")
                            print("-/Rs\n\n")
                        else:
                        #Else condition mentioned above is to withdrawl if thebalance is grater than the withdrawl amount
                        #withdraw Amount
                            balance=balance-withdrawl
                        #These statement updarte the statement in balane list
                            print("\n")
                            print("---Withdraw successful!---")
                            customerBalances[k]=balance
                            print("Your New balance:", balance,end=" ")
                            print("-RS\n\n")

            if j < 1:
        #the if condition above work for when the pin or 
             print("Your Name and pin does not match!\n")
             break
        mainMenu=input("please press enter key to go back to Mainmenu")
    elif choiceNumber== "3":
        
        
        print("choice Number 3 is selected by the customer")
        n=0
        #whie loop below would work when the pin or username 
        while n < 1:
            k= -1
            name=input("please input Name:")
            pin=input("please input pin:")

            while k < len(customerNames) -1:
                k=k + 1
                #the two if conditions below would find the balance
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        n=n +1 
                        #these statements below would show the customer Desposited balnce
                        #tge deposition made by the customer

                        print("Yoir Current Balance: ", end=" ")
                        print(customerBalances[k],end=" ")
                        print("/Rs")
                        balance=(customerBalances[k])
                        #this staement below takes the deposition from the customer balance
                        deposition=eval(input("Enter the value you want to deposit the amount"))
                        balance=balance+deposition
                        customerBalances[k]=balance
                        print("\n")
                        print("------your Deposition Successful")
                        print("your New Balance:", balance,end=" ")
                        print("-Rs\n\n")
            if n < 1:
                print("Your name and pin does not Maytch!\n")
                break
        mainMenu=input("please press enter a key key to go back to Mainmenu ")
    elif choiceNumber == "4":
        print("choice Number 4 is selected by the customer")
        k=0
        print("customer name list and balances mentioned below:")
        print("\n")
        #The while loop below will keep running until all the conditions satisfied
        while k <= len(customerNames) -1:
            print("-> Customer=",customerNames[k])
            print("->.Balance=", customerBalances[k],end=" ")
            print("-/Rs")
            print("\n")
            k=k+1
        mainMenu=input("please press enter a key key to go back to Mainmenu ")
            
    elif choiceNumber == "5":
        print("choice Number 5 is selected")
        print("Thank you for Using our Banking System")
        print("\n")
        print("Thankyou for visiting StateBank OF INDIA")
        break
    else:
        print("invalid option selected by the customer")
        print("please try again! ")
        mainMenu=input("please press enter a key key to go back to Mainmenu ")


    


       



        









