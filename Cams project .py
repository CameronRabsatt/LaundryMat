## variables
laundryWeight = 0 # current weight of laundry
taxRate = 1.06 # the tax rate as decimal
costPerPound = .50 # the cost per pound of laundry in dollars
total = 0 
custId = ''
custList = {'rabsatt1234' : 0.00 } # dictionary that stores all of the customers and all their money spent(pre tax)
ownerInput = '' # base input used to start program


## Functions
def weight_Calc() : ## returns cost of laundry session
    total_weight = laundryWeight
    total_price = total_weight * costPerPound
    return total_price

def subTotalPrice() : ## returns cost of laundry with tax
    tot = laundryWeight * costPerPound
    subtot = tot * taxRate
    return subtot

print ('Welcome\n') 


while ownerInput != '4' :
    ##prints choices of services
    print("MENU\n\n1.Calculate the total\n2.update charges \n3.customer information\n4.Quit\n ")

    ## Owner chooses which option(s) are being purchased
    ownerInput = input('Please select an option: ')## lets owner know what they select
    
    
    while ownerInput == '1' : #calculates the total 
      
        laundryWeight = float(input('Enter total weight of laundry in lbs: ')) ##Customer enters amount of laundry 
        custId = input('Input your customer id (last name with last 4 of phone number): ') #finds customers user id
        
        if custId in custList : ## checks for existing user id
            custList[custId] = custList[custId] + (weight_Calc()) ## adds current transaction to the total 
        else :
            custList[custId] = weight_Calc() ## creates value in dict and assigns weight
        
        print (f'\nTotal weight: {laundryWeight}Lbs  \nTotal price: ${weight_Calc():.2f} \nSubtotal price: ${subTotalPrice():.2f} ') ## prints customer recipt
        print (f'\nYour store total is {custList[custId]:.2f}') ## prints customers all time total at the store
        user_Quit = input('\nType "Q" to exit or "C" to continue : ')
       
        if user_Quit == 'q' or user_Quit == 'Q' : # gets user input to continue or end section 
            print ('Exiting Program\n')
            break
       
        elif user_Quit == 'c' or user_Quit == 'C':
            print ('\nNext total\n')
       
        else:
            print('Incorecct input, will quit\n')
            break 
    
    
    while ownerInput == '2' :

        changeStuff = input ('\n1. Change Tax Rate\n2. Change cost per pound\n3. Exit\nPlease select an option : ') ##allows user to decide what to change 
        
        if changeStuff == '1' :
            taxRate = (float(input('\nWhat would you like the new taxe rate to be? put in decimal form\n')) + 1) ## creates new tax rate according to change
            print (f'Your new tax rate is: {((taxRate - 1) * 100):.2f}%\n')
       
        elif changeStuff == '2' :
            costPerPound = float(input('\nWhat would you like the new cost per pound to be : '))## creates new cost 
            print (f'Your new cost per pound is: {costPerPound:.2f}$\n')
       
        elif changeStuff == '3' :
            print('Exiting Program\n')
            break 
       
        else :
            print("Incorrect input\nPlease try again")
   
   
    while ownerInput == '3' : 
        
        for cust in custList:
            print(f'\n{cust} has spent ${custList[cust]:.2f}')# prints complete customer list
        dicInput = input('\nTo reprint type "yes" \nTo return to menu type "no" : ') ## gets input on wether to reprint or not
       
        if dicInput == 'yes' or dicInput =='Yes' :
            print('\nYou will reprint\n')
       
        elif dicInput == 'No' or dicInput == 'no'   :
            print('\nYou will exit\n')
            break
       
        else :
            print('\nIncorect input,Exiting...\n')
            break
   
   
    while ownerInput == '4' :
        print ('Exiting Program')#closses app 
        break
    
    
    if ownerInput != '1' and ownerInput != '2' and ownerInput != '3' and ownerInput != '4' : ## triggers when input is incorect
        print('\nERROR\n')