import yaml



# Load the YAML file
with open('/Users/jmore/MeSo/advertising-adbook-ingestion/src/airflow/dags/config/dev/s3.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Print the value of s3_key_date_pattern
print(config['s3_key_date_pattern'])



with open('testfile', 'w') as file:
    file.write('This is a test file')
    file.write('This is a test file')
    file.write('This is a test file')
    file.close()


