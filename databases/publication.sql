CREATE TABLE publications (
	publication_id INTEGER PRIMARY KEY AUTOINCREMENT,
	publication_title VARCHAR(256),
	published_date VARCHAR(50),
	journal VARCHAR(50),
	doi VARCHAR(50),
	study_id VARCHAR(50),
	study_name VARCHAR(50),
	PMID INTEGER,
	link_url VARCHAR(50),
	file_link VARCHAR(50)
);

CREATE TABLE all_contributors (
	full_name VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	short_name VARCHAR(50),
	organization VARCHAR(4)
);

CREATE TABLE authors (
	short_name VARCHAR(50),
	author_role VARCHAR(50),
	id INTEGER,
	FOREIGN KEY (id) REFERENCES publications(publication_id)
);

--DROP TABLE publications
--DROP TABLE all_contributors
--DROP TABLE authors