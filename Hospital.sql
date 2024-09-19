CREATE DATABASE hospital;
USE hospital;
CREATE TABLE patient_data (
    Id VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Email_Id VARCHAR(100),
    Phone_no VARCHAR(15),
    Address VARCHAR(255),
    Disease VARCHAR(100)
);
