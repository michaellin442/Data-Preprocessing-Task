import pandas as pd 
import sqlite3
import re

db = sqlite3.connect("databases/publications.db")

#run publications.sql to create the databases
try:
    with open("databases/publication.sql", 'r') as sql_file:
        sql_script = sql_file.read()
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()

except:
    print("\nDatabase already exists. Deleting and creating new database.")
    with open("databases/delete_tables.sql", 'r') as sql_file:
        sql_script = sql_file.read()
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()
    with open("databases/publication.sql", 'r') as sql_file:
        sql_script = sql_file.read()
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()

#define functions add data to database
def add_author(conn, contributor):
    sql = '''INSERT INTO all_contributors(full_name,first_name,last_name,short_name,organization,is_associate,is_refered)
             VALUES(?,?,?,?,?,?,?)'''
    cur = db.cursor()
    cur.execute(sql, contributor)
    db.commit()
    return cur.lastrowid

def add_publication(conn, publications):
    sql = '''INSERT INTO publications(publication_id,publication_title,published_date,journal,doi,study_id,study_name,PMID,link_url,file_link)
             VALUES(?,?,?,?,?,?,?,?,?,?)'''
    cur = db.cursor()
    cur.execute(sql, publications)
    db.commit()
    return cur.lastrowid

def add_publication_author(conn, authors):  
    sql = '''INSERT INTO authors(short_name,author_role,publication_id)
             VALUES(?,?,?)'''
    cur = db.cursor()
    cur.execute(sql, authors)
    db.commit()
    return cur.lastrowid

#import non-PHRI associates excel data to databases
print("\nLoading data...")
authors_dataframe = pd.read_excel("input_files/PHRI Authors List.xlsx", header=None, usecols=[0,1], sheet_name = "non - Associate", na_filter=False)
for row in authors_dataframe.itertuples(index=None):
    names = list(row)
    short_name = names[1]
    full_name = names[0]
    if full_name == "":
        long_name = (names[1]).split(' ')
        last_name = long_name[0]
        first_name = long_name[1]
    else: 
        long_name = (names[0]).split(',')
        if len(long_name) > 1:
            last_name = long_name[0]
            first_name = long_name[1].strip()
        else:
            long_name = names[1].split()
            last_name = long_name[0]
            first_name = long_name[1].strip()

    contributor = (full_name,first_name,last_name,short_name,"","True","True")
    add_author(db, contributor)

#import PHRI associates excel data to databases
PHRI_authors_dataframe = pd.read_excel("input_files/PHRI Authors List.xlsx",sheet_name = "Associate", usecols=(0,2), header = None, na_filter=False) 
for row in PHRI_authors_dataframe.itertuples(index=None):
    names = list(row)
    short_name = names[1]
    full_name = names[0]
    if full_name == "":
        long_name = (names[1]).split(' ')
        last_name = long_name[0]
        first_name = long_name[1]
    else: 
        long_name = (names[0]).split(',')
        if len(long_name) > 1:
            last_name = long_name[0]
            first_name = long_name[1].strip()
        else:
            long_name = names[1].split()
            last_name = long_name[0]
            first_name = long_name[1].strip()

    contributor = (full_name,first_name,last_name,short_name,"PHRI","True","True")
    add_author(db, contributor)

#import publications data to databases
publications_dataframe = pd.read_csv("input_files/publications.csv") 
for row in publications_dataframe.itertuples(index=None):
    values = list(row)
    publication_id = values[0]
    publication_title = values[1]
    published_date = values[3]
    journal = values[4]
    doi = values[5]
    study_id = values[6]
    study_name = values[7]
    PMID = values[8]
    link_url = values[9]
    file_link = values[10]
    publication = (publication_id,publication_title,published_date,journal,doi,study_id,study_name,PMID,link_url,file_link)
    add_publication(db, publication)

    pub_authors = re.split(r',|;', values[2])
    for i in pub_authors:
        short_name = i.strip()
        if pub_authors.index(i) == 0:
            author_role = "First Listed Author"
        elif pub_authors.index(i) == (len(pub_authors)-1):
            author_role = "Last Author"
        else: 
            author_role = "Co-Author"
        authors = (short_name,author_role,publication_id)
        add_publication_author(db, authors)

print("\nData loaded. Please run to_excel.py.")
db.close()
