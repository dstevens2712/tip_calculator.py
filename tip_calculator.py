print("Welcome To David's Tip Calculator")
pretax_ammount = float(input("Enter Pre-tax total "))#Enter the pretax total and convert to float
pre_tip_total = pretax_ammount * 1.10 # Used the pretax value to determine the total bill with tax. Tax is 10% multiply the bill by 1.10 to get the bill plus tax.
tip_as_a_decimal = ()       # Created an tip_as_a_decimal as an open variable
def convert_tip_percent_to_a_decimal():  #Created a function to take an inputed percent value, convert it to decimal form. 
    global tip_as_a_decimal        #Sets tip_as_a_decimal to a global variable
    enter_tip = float(input("Enter the percent of the pre-tax bill you would like to give as a tip: ")) #Takes the tip percent input from the user
    change_tip = input("Would you like to change the tip amount? Enter y for Yes: ")  # Asks the user if they would like to change the tip amount
    if 'y' in change_tip:                                                             #If the user enters y this block of code will be executed
        changed_tip = float(input("Enter the percent of the pre-tax bill you would like to give as a tip: ")) #Asks the user to input the new tip percent
        change_tip = input("Would you like to change the tip amount? Enter y for Yes: ") #Asks the user if they would like to change the tip percent
        changed_tip = changed_tip / 100         #takes the user input and converts it to decimal form     
        tip_as_a_decimal = changed_tip          #sets the changed tip value and assigns it to the global variable 
        print(tip_as_a_decimal)                 #prints out the tip percent converted to decimal form
    else:                                       #if the user inputs anything except y
        tip_as_a_decimal = enter_tip / 100      #takes the user input and converts it to decimal form 
        print(tip_as_a_decimal)                 #takes the user input and converts it to decimal form              

convert_tip_percent_to_a_decimal()             #This line activates our function

total_tip = float(pretax_ammount * tip_as_a_decimal) #multiply pretax amount and tip convert to float 
number_of_tippers = float(input("Enter number of Tippers "))#enter number of people tipping
tip = float(total_tip / number_of_tippers)           #divide total number of tip by the number of people tipping convert to float
print(f'Total Bill with tip is: ${total_tip + pre_tip_total} ') #print the total bill
print("Tip amount for each person $", round(tip, 2)) #print the tip amount for each person rounded to two decimal places
tip_plus_total = float(pre_tip_total + total_tip)/ number_of_tippers #calculates the total amount each person owes
print("Total each person has to pay $", round(tip_plus_total, 2))    #print the total amount each person owes rounded to two decimal places