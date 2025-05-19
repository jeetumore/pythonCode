import pandas as pd
#
#
HEADER_LIST = ["adbook_campaign_id", "version_number", "oracle_customer_id", "payment_term_days_count",
               "campaign_currency_code", "invoice_line_quantity", "invoice_line_description",
               "invoice_line_unit_price_amount_local", "campaign_name", "total_campaign_amount_local",
               "campaign_start_date", "campaign_end_date", "adbook_drop_id", "line_item_start_date",
               "line_item_end_date", "payment_method_value", "billing_term_value", "invoice_line_notes_text",
               "invoice_notes_text", "invoice_number", "invoice_date_pst", "invoice_type_value",
               "oracle_customer_profile_id", "oracle_contact_name_id", "additional_email_address",
               "adbook_campaign_participant_id", "customer_name", "billing_address", "billing_city", "billing_state",
               "billing_country", "billing_postal_code", "billing_contact_first_name", "billing_contact_last_name",
               "billing_contact_email_address", "billing_contact_phone", "tax_registration_number",
               "additional_tax_registration_number", "tax_calculation_date_pst", "capability_name",
               "invoice_print_status_flag", "campaign_reporting_year_number", "campaign_reporting_month_number",
               "line_number", "total_line_count", "source_system_invoice_id", "event_line_id",
               "invoice_reference_number", "adjustment_reason", "io_number"
               ]
#
# qubole_result_file = 'inputs.csv'
#     # with open(qubole_result_file, 'wb') as writer:
#     #     dataclasses = writer.read()
#
# with open(qubole_result_file, 'r') as reader:
#     data = reader.read()
#
# with open(qubole_result_file, 'w') as writer:
#     writer.writelines(data)


# qubole_result_file = 'inputs.csv'
# qubole_result_file1 = 'output8.csv'
# # Step 1: Preprocess the file to fix unmatched quotes
# with open(qubole_result_file, 'r') as reader:
#     lines = reader.readlines()
#
#
#
# cleaned_lines = []
# for line in lines:
#     # Replace triple quotes (""") with single quotes (")
#     line = line.replace('"""', '"')
#     # Fix unmatched quotes by closing them (example: "11 Lemoyne Ave -> "11 Lemoyne Ave")
#     if line.count('"') % 2 != 0:
#         line = line.rstrip() + '"'  # Append a closing quote
#         print(line)
#     cleaned_lines.append(line)
#
# # Step 2: Write the cleaned data back to the file
#
#
#
# df = pd.read_csv(qubole_result_file1, sep='\t', names=HEADER_LIST,
#                  index_col=False, na_values="\\N", keep_default_na=False, dtype=str)
# #
# with open(qubole_result_file1, 'w') as writer:
#     writer.writelines(cleaned_lines)

# with open('output7.csv', 'w') as writer:
#     writer.write(data)



import pandas as pd
import csv
import re

# # Step 1: Define a function to preprocess the file
# def preprocess_csv(file_path, output_path):
#     with open(file_path, 'r') as infile:
#         data = infile.read()
#
#         # Fix improper triple quotes in the file
#         cleaned_data = re.sub(r'"""\s*([^"]+)', r'"\1', data)
#         cleaned_data1 = re.sub(r'(?<!")"(.*?)$', r'"\1"', cleaned_data)
#         # print(cleaned_data)
#
#
#
#
#     # Write the cleaned data back to a temporary file
#     with open(output_path, 'w') as outfile:
#         outfile.write(cleaned_data1)
#
# # Step 2: Define the file paths
# input_file = 'inputs.csv'
# output_file = 'output9.csv'
#
# # Step 3: Preprocess the CSV
# preprocess_csv(input_file, output_file)
#
# # Step 4: Load the cleaned file with pandas
# try:
#     df = pd.read_csv(output_file, sep='\t', names=HEADER_LIST,
#                      index_col=False, na_values="\\N", keep_default_na=False, dtype=str)
#     print(df.head(9301))
# except pd.errors.ParserError as e:
#     print("ParserError:", e)


# def fix_unbalanced_quotes(inputs, output11):
#     with open('inputs.csv', 'r') as infile, open('output11.csv', 'w', newline='') as outfile:
#         reader = csv.reader(infile)
#         writer = csv.writer(outfile)
#
#         for row in reader:
#             fixed_row = []
#             for col in row:
#                 if col.startswith('"'):
#                     col = col[1:]
#                 if col.endswith('"'):
#                     col = col[:-1]
#                 fixed_row.append(col)
#             writer.writerow(fixed_row)

def clean_csv(inputs, output):
    with open(inputs, mode='r', newline='', encoding='utf-8') as infile, \
            open(output, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter=',', quotechar='"')
        #delimiter=',': Specifies that the delimiter between fields in the CSV file is a comma.
        #quotechar='"': Specifies that double quotes are used to quote fields in the CSV file.
        #quoting=csv.QUOTE_MINIMAL: Specifies that fields will only be quoted
        # if they contain special characters such as the delimiter or the quote character.
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            cleaned_row = []
            for cell in row:
                original_cell = cell
                # Remove unclosed quotes and any extra quotes
                cleaned_cell = cell.replace('"""', '').replace('"', '')
                if original_cell != cleaned_cell:
                    print(f"Line: {original_cell} -> {cleaned_cell}")
                cleaned_row.append(cleaned_cell)
            writer.writerow(cleaned_row)


clean_csv('inputs.csv', 'output13.csv')
df = pd.read_csv('output14.csv', sep='\t', names=HEADER_LIST,
                 index_col=False, na_values="\\N", keep_default_na=False, dtype=str)



# Remove JNDI issue bad-data
bypass_string = "java.lang.ClassNotFoundException: org.apache.logging.log4j.core.lookup.JndiLookup"
print(type(df))
if df.iloc[0].str.contains(bypass_string).any():
    # Drop the first row
    df = df.drop(df.index[0])

    print(df)

df = pd.read_csv('output13.csv', sep='\t', names=HEADER_LIST,
                 index_col=False, na_values="\\N", keep_default_na=False, dtype=str)

