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

    # Create an Excel writer object
    with pd.ExcelWriter('output.xlsx') as writer:
        # DataFrame to store the current section
        df = pd.DataFrame(columns=['Item Number', 'Context'])

        # Sheet name for the current section
        sheet_name = 'Main'

        # Temporary variable to store context
        context = ''

        # Iterate through the lines and extract item numbers and context
        for line in lines:
            # Check if the line starts a new section
            if any(keyword in line for keyword in ["ANEXOS AO EDITAL", "APÊNDICE DO ANEXO",
                                                   "ANEXO II - REMUNERAÇÃO BASEADA EM SPRINTS EM METODOLOGIA ÁGIL",
                                                   "ANEXO III - INFORMAÇÕES PARA DIMENSIONAMENTO DE INFRAESTRUTURA",
                                                   "ANEXO IV - PROCESSO DE AMOSTRA DA FERRAMENTA"]):
                # Save the current section to a sheet
                if not df.empty:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

                # Start a new DataFrame for the new section
                df = pd.DataFrame(columns=['Item Number', 'Context'])

                # Set the sheet name for the new section
                sheet_name = line.strip()[:31]  # Limit to 31 characters for Excel

            # Match item numbers and context
            match = re.match(r'(\d+(\.\d+)*)\.\s+(.*)', line)
            if match:
                item_number, _, new_context = match.groups()
                if context:
                    df.loc[len(df)] = [item_number, context]
                context = new_context
            else:
                context += ' ' + line

        # Save the last section to a sheet
        if context:
            df.loc[len(df)] = [item_number, context]
        if not df.empty:
            df.to_excel(writer, sheet_name=sheet_name, index=False)