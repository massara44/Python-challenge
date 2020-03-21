# Importing modules    
import os
import csv


#loading file
pybank_path = os.path.join("Resources", "budget_data.csv" )

#variables for total months, amount, value, change, dates and profits
total_month = 0

#variables for total amount
total_amount = 0

#variable for value
value = 0

#variable for change
change = 0

#variable for dates
dates = []

#variable for profits
profits = []

#Opening file
with open(pybank_path) as csvfile:
    csv_reader = csv.reader(csvfile)

    #first line has header value
    header = next(csv_reader)
   

    # Extract first row 
    firstrow = next(csv_reader)

    total_month += 1
    total_amount += int(firstrow[1])

    value = int(firstrow[1])
 

    for row in csv_reader:
        total_month += 1
        total_amount += int(firstrow[1])

        #tracking the dates
        dates.append(row[0])
        
        #calculate the change, then add it to list
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
    

    #Greatest increase in profits
    gr_profits = max(profits)
    gr_index = profits.index(gr_profits)
    gr_date = dates[gr_index]


    #Greatest decrease in profits 
    gr_losses = min(profits)
    gl_index = profits.index(gr_losses)
    gl_date = dates[gl_index]


    #average change in Profit/Losses over the entire period
    avg_change = sum(profits)/len(profits)

    #displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_month)}")
print(f"Total: ${str(total_amount)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {gr_date} (${str(gr_profits)})")
print(f"Greatest Decrease in Profits: {gl_date} (${str(gr_losses)})")

