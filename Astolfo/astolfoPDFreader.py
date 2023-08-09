import PyPDF2
import pandas as pd
import re

# Open the PDF file
with open('Astolfo/edital.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Read the text from all pages
    text = ''
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()

    # Split the text into lines
    lines = text.split('\n')

    # Define a pattern to match item numbers and context, including sub-numbering
    pattern = re.compile(r'(\d+(\.\d+)*)\.\s+(.*)')

 # Create an Excel writer object
with pd.ExcelWriter('output.xlsx') as writer:  # Use 'with' statement
    # DataFrame to store the current section
    df = pd.DataFrame(columns=['Item Number', 'Context'])

    # Sheet name for the current section
    sheet_name = 'Main'

    # Iterate through the lines and extract item numbers and context
    for line in lines:
        # Check if the line starts a new section
        if "ANEXOS AO EDITAL" in line:
            # Save the current section to a sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Start a new DataFrame for the new section
            df = pd.DataFrame(columns=['Item Number', 'Context'])

            # Set the sheet name for the new section (e.g., "ANEXO I - TERMO DE REFERÊNCIA")
            sheet_name = line.strip()
        if "APÊNDICE DO ANEXO" in line:
            # Save the current section to a sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Start a new DataFrame for the new section
            df = pd.DataFrame(columns=['Item Number', 'Context'])

            # Set the sheet name for the new section (e.g., "ANEXO I - TERMO DE REFERÊNCIA")
            sheet_name = line.strip()
        if "ANEXO II - REMUNERAÇÃO BASEADA EM SPRINTS EM METODOLOGIA ÁGIL" in line:
            # Save the current section to a sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Start a new DataFrame for the new section
            df = pd.DataFrame(columns=['Item Number', 'Context'])

            # Set the sheet name for the new section (e.g., "ANEXO I - TERMO DE REFERÊNCIA")
            sheet_name = line.strip()
        if "ANEXO III - INFORMAÇÕES PARA DIMENSIONAMENTO DE INFRAESTRUTURA" in line:
            # Save the current section to a sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Start a new DataFrame for the new section
            df = pd.DataFrame(columns=['Item Number', 'Context'])

            # Set the sheet name for the new section (e.g., "ANEXO I - TERMO DE REFERÊNCIA")
            sheet_name = line.strip()
        if "ANEXO IV - PROCESSO DE AMOSTRA DA FERRAMENTA" in line:
            # Save the current section to a sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Start a new DataFrame for the new section
            df = pd.DataFrame(columns=['Item Number', 'Context'])

            # Set the sheet name for the new section (e.g., "ANEXO I - TERMO DE REFERÊNCIA")
            sheet_name = line.strip()

        # Match item numbers and context
        match = pattern.match(line)
        if match:
            item_number, _, context = match.groups()
            df.loc[len(df)] = [item_number, context]

    # Save the last section to a sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)