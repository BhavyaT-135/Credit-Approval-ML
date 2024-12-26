import pandas as pd

# Specify the path to your .dat file
input_file = 'data.txt'
output_file = 'data.xlsx'

# Read the .dat file
data = pd.read_csv(input_file, delim_whitespace=True, header=None)

print(data)

# # Define column names (you can customize these names if needed)
# column_names = [f'Variable_{i}' for i in range(1, 16)]
# data.columns = column_names

# # Write the data to an Excel file
# data.to_excel(output_file, index=False)

# print(f"Data has been successfully written to {output_file}")