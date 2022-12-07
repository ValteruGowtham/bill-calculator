#in this project
    #it will how much bill you hav eyo pay
bill=int(input("how much is your bill amount:"))
tip=int(input("how much percentage of tip you want to give:"))
mem=int(input("in how many people you want to divide:"))
tip_bill=tip/100 * bill 
total_bill=tip_bill + bill
total_bill_per_person=total_bill / mem
final_bill=round(total_bill_per_person,2)
print("amount paid per each person: ",final_bill)
