'''                             Practical Task
Follow these steps:
● Imagine you are running a cafe. Create a new Python file in your folder
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the cafe.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the total_stock worth in the cafe. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
Tip: When you loop through the menu list, the ‘items’ can be set as keys
to access the corresponding ‘stock’ and ‘price’ values. Each ‘item_value’ is
calculated by multiplying the stock value by the price value. For example:
item_value = (stock[items] * price[items])
'''

# First we are going to make a list that contains four items
menu = ['Tea', 'Coffee', 'Eggs', 'Cake']

# Creating a dictionary that contains the stock value for each item
stock = {'Tea': 200, 'Coffee': 150, 'Eggs': 50, 'Cake': 20}

# Creating a dictionary that contains prices for each item on the menu
price = {'Tea': 2.00, 'Coffee': 3.50, 'Eggs': 3.99, 'Cake': 4.00}

# Calculating the total stock worth in the cafe
total_stock = 0


# To calculate total stock worth we have to loop through the menu 
for item in menu:
    item_value = stock[item] * price[item] #total stock multiply by price
    total_stock += item_value

# In this line the total stock in the cafe will be printed 
print(f"The Total stock in the cafe is worth : £{total_stock:.2f}") # Printing the total stock in the cafe with 2 decimal floating point.

# Or simply printing in a different way
print("The Total stock in the cafe is worth : £",float(total_stock))



'''I hope my formula and calculation is correct ,it gives me the result 
but when i calculate manually it actually gives me a different result.
If i miss anything please leave me a feedback. Kind regards
'''