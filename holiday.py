# Calculate a user's total holiday cost

# User inputs
#  1. What city they will be flying to - city_flight
city_flight = input("""Which city will you be flying to: "
                    1. Cape Town
                    2. Tokyo
                    3. New York
                    4. Toronto
                    """ )

# 2. The number of nights at the hotel - num_nights
num_nights = int(input("How many nights will you be staying at the hotel? "))

# 3. The number of days the user will be hiring a car - rental_days
rental_days = int(input("How many days will you be hiring a car? "))

#Create four functions:
# 1. hotel_cost():
def hotel_cost(num_nights):
    cost_per_night = 500
    return num_nights * cost_per_night

# 2. plane_cost():
def plane_cost(city_flight):
    if city_flight.lower() == "cape town":
        return 1000
    elif city_flight.lower() == "tokyo":
        return 1500
    elif city_flight.lower() == "new york":
        return 2000
    elif city_flight.lower() == "toronto":
        return 2500
    else:
        return 2500
        # If city is not mentioned in the above list

# 3. car_rental():
def car_rental(rental_days):
    rental_cost_per_day = 100
    return rental_days * rental_cost_per_day

# 4. Holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    num_nights = hotel_cost(num_nights)
    city_flight = plane_cost(city_flight)
    rental_days = car_rental(rental_days)
    holiday_cost = num_nights + city_flight + rental_days
    return holiday_cost

# 5. Print the total cost of the holiday 
#    Print("The total cost for your holiday is: R", holiday_cost(city_flight,num_nights,rental_days))
print(f"The total cost for your holiday is R {holiday_cost}")