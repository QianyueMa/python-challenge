# Dependencies
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
outputpath = os.path.join('..', 'PyBank', 'analysis', 'budget_analysis.txt')


# Count the total number of months included in the dataset
with open(csvpath) as csvfile:
    num_rows = 0
    for row in open(csvpath):
        num_rows += 1

num_months = num_rows - 1 # Not counting the header row of the sheet
print(f"Total Months: {num_months}") 



# Count the net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:

    revenue = csv.reader(csvfile)
    csv_header = next(revenue) # to skip the header (strings not integers)

    total = 0
    for row in revenue: 
        total += int(row[1])
print (f"Total: ${total}")



# Calculate the average of the changes in "Profit/Losses" over the entire period
avg_change = total / num_months
print(f'Average Change: ${avg_change}')



# The greatest profit/loss
with open(csvpath) as csvfile:

    revenue = csv.reader(csvfile)
    csv_header = next(revenue) 

    changes = list(revenue)

greastest_profit = max(changes, key=lambda row: int(row[1]))
greastest_loss = min(changes, key=lambda row: int(row[1]))

# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {greastest_profit}')
# The greatest increase in losses (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {greastest_loss}')


# Export the outputs; the txt file is in the "analysis" folder
export_output = (
    f"\nFinancial Analysis\n"
    f"--------------------------------\n"
    f"Total Months: {num_months}\n"
    f"Total Revenue: ${total}\n"
    f"Average Revenue Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {greastest_profit}\n"
    f"Greatest Decrease in Profits: {greastest_loss}\n"
    )

print (export_output)

with open(outputpath, "w") as txt_file:
    txt_file.write(export_output)
