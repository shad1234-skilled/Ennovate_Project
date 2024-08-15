
-- SQL Schema and Sample Data Script

-- Drop tables if they exist to avoid conflicts during re-execution
DROP TABLE IF EXISTS housing_data;
DROP TABLE IF EXISTS predictions;

-- Create table for housing data
CREATE TABLE housing_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_sqft REAL,
    bath INTEGER,
    price REAL,
    location TEXT,
    bhk INTEGER
);

-- Create table for predictions
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    total_sqft REAL,
    bath INTEGER,
    bhk INTEGER,
    predicted_price REAL
);

-- Insert sample data into housing_data
INSERT INTO housing_data (total_sqft, bath, price, location, bhk) VALUES
(1056.0, 2, 39.07, 'alandi road', 2),
(2894.0, 4, 245.00, 'alandi road', 4),
(1084.0, 2, 50.00, 'alandi road', 2),
(1000.0, 2, 25.00, 'alandi road', 2),
(1230.0, 2, 80.00, 'alandi road', 2);

-- Insert sample data into predictions
INSERT INTO predictions (location, total_sqft, bath, bhk, predicted_price) VALUES
('pashan', 1200, 2, 2, 100.00),
('alandi road', 1056, 2, 2, 39.07),
('pashan', 1500, 3, 3, 120.00);
