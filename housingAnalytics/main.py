import pandas as pd
import matplotlib.pyplot as plt

approved = 0
denied = 0

# Load your dataset
data = pd.read_csv('HackUTD-2023-HomeBuyerInfo.csv')

# Define the boolean variables to determine what criteria fit
results = []


# Define the approval criteria (you can customize this based on your requirements)
def is_eligible(applicant):
    global approved, denied
    credit_score = applicant['CreditScore']
    monthly_mortgage_payment = applicant['MonthlyMortgagePayment']
    if applicant['LTV'] > 0.80:
        PMI = 1 + (.01 / 12)
        monthly_mortgage_payment += (applicant['AppraisedValue'] * PMI)
    FEDTI = monthly_mortgage_payment / applicant['GrossMonthlyIncome']

    # Define the approval criteria (you can customize this based on your requirements)
    creditScoreTest = (credit_score >= 640)
    LTV_Test = (applicant['LTV'] < 0.95)
    DTI_Test = (applicant['DTI'] <= 0.36)
    FEDTI_Test = (FEDTI <= 0.28)

    eligible = False

    if creditScoreTest and LTV_Test and DTI_Test and FEDTI_Test:
        approved+=1
        results.append("Approved")
        eligible = True;
    else:
        denied += 1
        reasons = []
        if not creditScoreTest:
            reasons.append("Increase your credit score!")
        if not LTV_Test:
            reasons.append("Lower the loan cost!")
        if not DTI_Test:
            reasons.append("Lower your debt-to-income ratio!")
        if not FEDTI_Test:
            reasons.append("Lower your mortgage-to-income ratio!")

        results.append(", ".join(reasons))


# Apply the approval criteria to each row in the dataset
for index, row in data.iterrows():
    applicant = {
        'CreditScore': row['CreditScore'],
        'LTV': row['LoanAmount'] / row['AppraisedValue'],
        'DTI': (row['CreditCardPayment'] + row['CarPayment'] + row['StudentLoanPayments']) / row['GrossMonthlyIncome'],
        'MonthlyMortgagePayment': row['MonthlyMortgagePayment'],
        'GrossMonthlyIncome': row['GrossMonthlyIncome'],
        'AppraisedValue': row['AppraisedValue']
    }
    is_eligible(applicant)

# Add the results to the DataFrame
data['LoanStatus'] = results

# Save the DataFrame with loan status
data.to_csv('LoanStatusResults.csv', index=False)

# Calculate percentages
total_cases = approved + denied #should be 10,000
approved_percentage = (approved / total_cases) * 100
denied_percentage = (denied / total_cases) * 100

# Create a bar chart
categories = ['Approved', 'Denied']
percentages = [approved_percentage, denied_percentage]

plt.bar(categories, percentages)
plt.title('Loan Approval Status')
plt.ylabel('Percentage')
plt.show()

print("Approved: {:.2%}".format(approved / 10000))
print("Denied: {:.2%}".format(denied / 10000))


