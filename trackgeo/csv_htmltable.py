import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv('csv_raw.csv')

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False)

# Save the HTML table to a file
with open('output.html', 'w') as f:
    f.write(html_table)
