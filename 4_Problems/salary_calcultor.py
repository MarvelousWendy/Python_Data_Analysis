# salary calculator
def calculate_salary(hourly_rate, hours_per_week, bonus=0.1):
    weekly_salary = hourly_rate * hours_per_week
    annual_salary = weekly_salary * 52
    return annual_salary + (annual_salary * bonus)
