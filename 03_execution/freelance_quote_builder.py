def main():
    # Get inputs
    client_name = input("Client name: ")
    client_name = client_name.strip().title()
    work_hours = float(input("Estimated work hours: "))
    hourly_rate = float(input("Hourly rate: "))
    expenses = float(input("additional expenses: "))
    # Calculate estimates
    labor_cost = estimate_labor_cost(work_hours, hourly_rate)
    estimate = labor_cost + expenses
    # Format text
    hourly_rate = format_text(hourly_rate)
    expenses = format_text(expenses)
    labor_cost = format_text(labor_cost)
    estimate = format_text(estimate)
    # Output text
    print("\nPROJECT ESTIMATE")
    print("CLIENT: " + client_name)
    print("LABOR COST: " + labor_cost)
    print("DIRECT EXPENSES: " + expenses) 
    print("ESTIMATE: " + estimate)

def estimate_labor_cost(hours, rate):
    return hours * rate

def format_text(value):
    value = ("$" + f"{value:.2f}")
    return value

main()