# Engineering Design

**Team members:**
Garrett Capps & Johnney Tovar
Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type.*
string client_name 
float work_hours
float hourly_rate
integer expenses

## Processing

*What calculations, text clean up, numberic converstions, ext will the program perform on the inputs?*


```text
--Calculations--
1. Multiply work_hours by hourly_rate to get estimated labor cost and store to a new variable, float labor_cost.
2. Add float expenses to labor_cost to get final estimate, float estimate
--Formatting--
1. Clean up inputted client name; client_name = client_name.strip().title()
2. Format number values; I.e. hourly_rate = ("$" + f"{labor_cost:.2f}")

```

## Output

*What will the program display? How will you format it?*
Output required header, "PROJECT ESTIMATE"
Output required values in order:
Client name
Labor cost
Direct Expenses
Total Estimate
## Functions

*Describe `main()` and at least one calculation function. For each, give its name, purpose, parameters, and returned result (or none).*
function estimate_labor_cost() which will take the input values of work_hours and hourly_rate and return the estimated labor cost
function format_text(), which will take a float value and return it as a properly formatted string
main(), which will prompt the user for input, call the other functions, calculate estimate, and print the output to the user