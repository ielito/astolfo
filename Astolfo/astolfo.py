import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the questions
#questions = [
#    "Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password",
#    "Ensure console credentials unused for 90 days or greater are disabled",
#    # Add other questions here
#]

import pandas as pd

# Path to the Excel file containing the questions
xlsx_file_path = 'Astolfo/CloudControls.xlsx'

# Read the questions from the Excel file
questions_df = pd.read_excel(xlsx_file_path)

# Extract the questions from the specific column (replace 'Your Column Name' with the actual column name)
questions = questions_df['CONTROL NAME'].tolist()
 

# Define the URLs for compliance requirements
urls = {
    "ISO27001": "https://www.itgovernance.co.uk/blog/iso-27001-the-14-control-sets-of-annex-a-explained",
    "SOC2": "https://www.logicmanager.com/resources/compliance-management/download-soc-2-compliance-checklist/",
    "HIPAA": "https://www.hipaajournal.com/hipaa-compliance-software/",
    "PCI-DSS": "https://docs.cgn.portal.checkpoint.com/docs/d9_aws_iam_08",
    # Add other URLs here
}

# Create a DataFrame to store the results
df = pd.DataFrame(columns=["Questions", "Security Compliance Attempts", "Report Containing Feature", "Evidence/Link"])
df["Questions"] = questions

# Iterate through the URLs and scrape the data
for compliance, url in urls.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Analyze the content of the page and identify the relevant information
    # This part will vary depending on the structure of the web pages
    # You may need to customize this part to extract the specific information you need
    
    # Update the DataFrame with the information
    # Example:
    df.loc[df["Questions"] == "Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password", "Security Compliance Attempts"] = compliance
    # Repeat for other columns and questions

# Save the DataFrame to a CSV file
df.to_csv("Astolfo/compliance_table.csv", index=False)

print("Table created successfully!")
