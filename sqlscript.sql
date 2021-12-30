DROP TABLE PUBLICATION;
DROP TABLE EMPLOYEE;
DROP TABLE CREDENTIALS;

CREATE TABLE EMPLOYEE 
(
Emp_ID VARCHAR(12) NOT NULL,
Name VARCHAR(45) NOT NULL,
Category VARCHAR(45) NOT NULL,
Status_of_Target VARCHAR(45) NOT NULL,
PRIMARY KEY (Emp_ID)
);

CREATE TABLE PUBlICATION
(
	Emp_ID VARCHAR(12),
    Publisher_Name VARCHAR(20) NOT NULL,
    Type VARCHAR(30) NOT NULL,
    Status VARCHAR(100) NOT NULL,
    Title VARCHAR(200) NOT NULL,
    DOI VARCHAR(500),
    Pdate DATE,
    Affiliation VARCHAR(100) NOT NULL,
    Indexing VARCHAR(30) NOT NULL,
    FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEE(Emp_ID) ON DELETE SET NULL
);

CREATE TABLE CREDENTIALS
(	
	username varchar(50),
    password varchar(100),
    accesslevel integer
);

select Emp_ID from employee;
SELECT * FROM EMPLOYEE;
SELECT * FROM PUBLICATION;
SELECT * FROM CREDENTIALS;

INSERT INTO employee VALUES ("21324","admin","Test","Testing");
INSERT INTO employee VALUES ("223","efgh","c","d");
INSERT INTO publication VALUES (123,"abcd","a","b","c","d",2002/04/05,"mitwpu");
INSERT INTO publication VALUES (223,"efgh","c","d","e","f",2020/06/07,"mitwpu");
INSERT INTO credentials VALUES ("abcd@mitwpu.edu.in","123456",1);