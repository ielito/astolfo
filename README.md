# PDF to Excel Converter for Specific Sections

## Overview

This project provides a Python script to analyze security compliance questions against various regulatory standards such as ISO 27001, SOC 2, PCI-DSS, and HIPAA. It reads questions from a CSV file, searches for relevant information from specified URLs, and consolidates the findings into a table.

## Features

- Reads questions from a specified CSV file.
- Searches for compliance information from various regulatory standards.
- Consolidates findings into a table.
- Option to search within Google Drive for Excel files containing relevant information.

## Prerequisites

- Python 3.x
- Libraries: `pandas`, `requests`, `BeautifulSoup`, `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`, `openpyxl`, `PyPDF2`,

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd path/to/your/repository
   ```

3. Install the required libraries:

   ```bash
   pip install pandas requests beautifulsoup4 google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl PyPDF2
   ```

## Usage

1. Place the PDF file you want to convert in the same directory as the script or update the file path in the code.
2. Run the script:

   ```bash
   python yourscript.py
   ```
3. The script will create an Excel file named `output.xlsx` in the same directory

## How It Works

- The script reads the PDF file using PyPDF2 and extracts the text from all pages.
- It splits the text into lines and iterates through them to identify specific sections and item numbers.
- The content is organized into a pandas DataFrame, with each section saved as a separate sheet in the Excel file.
- Sheet names are determined by specific keywords found in the text, such as "ANEXOS AO EDITAL," "APÊNDICE DO ANEXO," etc.
- The context for each item number includes all lines until the next item number or the end of the section.

## Customization
You can customize the script to suit your specific needs by modifying the following:

- PDF File Path: Update the file path to the PDF you want to convert.
- Section Keywords: Modify the list of keywords that determine the start of a new section.
- Output File Name: Change the name of the Excel file that will be created.

## Code Overview
The main part of the code is as follows:

- Open the PDF and read the text.
- Split the text into lines and iterate through them.
- Identify new sections based on specific keywords.
- Match item numbers and concatenate the context until the next item number.
- Write each section to a separate sheet in the Excel file.

## Contributing

If you would like to contribute to this project, please feel free to fork the repository, create a feature branch, and submit a pull request.

Special thanks to:
- @cpmoura
- Arnold
- Codexius Maximus

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.