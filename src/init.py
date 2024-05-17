import pandas as pd 

#non-PHRI associates
print("\nNon-PHRI Associates\n----------------------------------")
authors_dataframe = pd.read_excel("input_files/PHRI Authors List.xlsx",sheet_name = "non - Associate", usecols=(0,1), header = None) 
print(authors_dataframe)

#PHRI associates
print("\nPHRI Associates\n----------------------------------")
PHRI_authors_dataframe = pd.read_excel("input_files/PHRI Authors List.xlsx",sheet_name = "Associate", usecols=(0,2), header = None) 
print(PHRI_authors_dataframe)

#publications
print("\nPublications\n----------------------------------")
publications_dataframe = pd.read_csv("input_files/publications.csv") 
print(publications_dataframe)

