import pandas as pd
import sqlite3

#export database to excel file "output.xlsx"
connection = sqlite3.connect("databases/publications.db")
query = """SELECT 
    authors.publication_id,
    authors.author_role, 
    (all_contributors.first_name || " " || all_contributors.last_name) as fullname,
    all_contributors.first_name,
    all_contributors.last_name,
    all_contributors.organization,
    all_contributors.is_associate,
    all_contributors.is_refered
FROM
    authors 
    JOIN all_contributors ON authors.short_name = all_contributors.short_name
    JOIN publications ON authors.publication_id = publications.publication_id
ORDER BY publications.publication_id"""
df = pd.read_sql(query, connection)
df.to_excel("output_files/output.xlsx")

print("\nData returned as excel sheet.")