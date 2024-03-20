'''
● Create a Python file called holiday.py.
● Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
● First, get the following user inputs:
○ city_flight: The city they will be flying to. (You can create some
options for them. Remember each city will have different flight
costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days for which they will be hiring a
car.
● Next, create the following four functions:
● hotel_cost: This function will take num_nights as an argument,
and return a total cost for the hotel stay (you can choose the price
per night charged at the hotel).
● plane_cost: This function will take city_flight as an argument
and return a cost for the flight. (Hint: use if/else if statements in
the function to retrieve a price based on the chosen city.)
● car_rental: This function will take rental_days as an argument
and return the total cost of the car rental (you can choose the daily
rental cost.)
● holiday_cost: This function will take the three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments, you can call all three of the above functions with
respective arguments and finally return a total cost for your
holiday.
● Print out all the details about the holiday in a readable way.
● Try running your program with different combinations of input to show
its compatibility with different options.'''

def hotel_cost(num_nights):
    # suppose we have a fixed price per night for the hotel
    price_per_night = 150 
    return num_nights * price_per_night

def plane_cost(city_flight):
    # Assigning random prices for cities
    if city_flight == "istanbol":
        return 500
    elif city_flight == "dubai":
        return 400
    elif city_flight == "paris":
        return 600
    else:
        return 300  # For other cities there is a default price which is 300

def car_rental(rental_days):
    # Suppose we have a fixed daily rental cost for the car
    daily_rental_cost = 60
    return rental_days * daily_rental_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

def main():
    # Request user inputs about city, number of nights and and renting a car for how many days.
    city_flight = input("Enter the city you will be flying to (e.g., istanbol, dubai, paris): ")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    # Calculating total costs for hotel, flight, and car rental in the following 4 lines of code.
    hotel_total_cost = hotel_cost(num_nights)
    plane_total_cost = plane_cost(city_flight)
    car_rental_total_cost = car_rental(rental_days)
    total_holiday_cost = holiday_cost(hotel_total_cost, plane_total_cost, car_rental_total_cost)

    # By using Print function we will print complete holiday package.
    print("\nComplete Holiday package and Cost:")
    print(f"City of Flight: {city_flight}")
    print(f"Hotel Cost: ${hotel_total_cost}")
    print(f"Flight Cost: ${plane_total_cost}")
    print(f"Car Rental Cost: ${car_rental_total_cost}")
    print(f"Total Holiday Cost: ${total_holiday_cost}")

if __name__ == "__main__":
    main()
