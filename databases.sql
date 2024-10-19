CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    university VARCHAR(100),
    score INT
);


INSERT INTO students (name, age, university, score) VALUES
('Ali Aliyev', 20, 'Bakı Dövlət Universiteti', 85),
('Aygün Hüseynova', 21, 'Azərbaycan Texniki Universiteti', 90),
('Kamran Məmmədov', 22, 'ADA Universiteti', 95);



