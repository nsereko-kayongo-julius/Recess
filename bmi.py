# #calculate the body mass index
height = input("what is your height\n ")
weight = input("what is your weight \n")
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print(f"{bmi} is under weight")
elif bmi < 25:
    print(f"{bmi} is normal weight")
elif bmi < 30:
    print(f"{bmi} is over weight")
elif bmi < 35:
    print(f"{bmi} is obese")
else:
    print(f"{bmi} is clinically obese")


# days weks and years left for one to live until 90 years
current_age = input("what is your current age \n")
target_age = 90
current_age_int = int(current_age)
remaining_years = 90 - current_age_int
remaining_weeks = remaining_years * 52
remaing_days = remaining_years * 365
remaining_months = remaining_years * 12
print(
    f"you have {remaing_days} days, {remaining_weeks} weeks, {remaining_months} months")

# Tip calculator
# print("welcome to tip calculator!")
# total_bill = input("what is your total bill ? $")
# tip = input("what percentage tip would you like to give ? 10, 12 or 15? ")
# people = input("how many people would you like to split the bill ? ")

# total_bill_float = float(total_bill)
# tip_percentage = (float(tip) + 100)/100
# people_int = int(people)

# totalbill_and_tip = total_bill_float * tip_percentage
# persaonal_pay = round((totalbill_and_tip / people_int), 2)

# print(f"each person should pay: ${persaonal_pay}")
