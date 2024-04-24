def zeller_formula(day, month, year):
    # January and February are counted as months 13 and 14 of the previous year
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
    
    # Zeller's Congruence formula
    k = year % 100  # year within the century
    c = year // 100  # century
    m= month
    d = day

    f=(k+((13*m-1)//5)+d+(d//4)+(c//4)-2*c)%7
    
    
    # Determine the day of the week based on f
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = days_of_week[f]
    
    return day_of_week

# Example usage:
day = int(input("enter the day:"))
month = int(input("enter the month:"))
year = int(input("enter the year:"))
if month%2==0:
    if day==31:
        print("invalid")
        exit()
if year>9999:
    print("wrong entry")
    exit()
day_of_week = zeller_formula(day, month, year)
print(f"The day of the week for {day}/{month}/{year} is: {day_of_week}")
