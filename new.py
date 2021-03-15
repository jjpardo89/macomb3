#Points the customer has earned input
points = int(input("Number of Customer Points:"))
discount = float()
#Calculation for finding the points and what discount they receive:
if points <= 50:
    discount = 0
elif points > 50 and points <= 100:
    discount = 0.1
elif points > 100 and points <= 200:
    discount = 0.2
elif points > 200 and points < 300:
    discount = 0.25
else:
    discount = 0.3
#input for the amount of years they've been a customer
customeryears = int(input("How many years have you been a customer: ")) 

#discount based on their years
if(customeryears >= 5):
    discount = discount + 0.05
#Final Discount
print("Customer Discount:", discount)