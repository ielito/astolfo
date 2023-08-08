# Compliance Analysis Tool

## Overview

This project provides a Python script to analyze security compliance questions against various regulatory standards such as ISO 27001, SOC 2, PCI-DSS, and HIPAA. It reads questions from a CSV file, searches for relevant information from specified URLs, and consolidates the findings into a table.

## Features

- Reads questions from a specified CSV file.
- Searches for compliance information from various regulatory standards.
- Consolidates findings into a table.
- Option to search within Google Drive for Excel files containing relevant information.

## Prerequisites

- Python 3.x
- Libraries: `pandas`, `requests`, `BeautifulSoup`, `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`, `openpyxl`

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
   pip install pandas requests beautifulsoup4 google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl
   ```

## Usage

1. Update the `csv_file_path` variable in the script with the path to the CSV file containing your questions.
2. Customize the `urls` dictionary with the URLs for the compliance requirements you want to analyze.
3. Run the script:

   ```bash
   python yourscript.py
   ```

## Contributing

If you would like to contribute to this project, please feel free to fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to anyone who contributed to the development of this project.

---

Feel free to modify and expand this README to include any additional information specific to your project. If you have any questions or need further assistance, please let me know!
