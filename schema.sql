-- Food Safety Intelligence demo database.
-- All entities and records below are fictional and synthetic.

CREATE DATABASE IF NOT EXISTS food_safety_system;
USE food_safety_system;

CREATE TABLE IF NOT EXISTS Restaurant (
    restaurant_name VARCHAR(100) PRIMARY KEY,
    rating DECIMAL(2,1) NOT NULL,
    total_orders INT NOT NULL,
    complaints INT NOT NULL,
    refunds INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_name VARCHAR(100) NOT NULL,
    sentiment ENUM('positive', 'negative') NOT NULL,
    FOREIGN KEY (restaurant_name) REFERENCES Restaurant(restaurant_name)
);

CREATE TABLE IF NOT EXISTS HygieneRules (
    signal_name VARCHAR(100) PRIMARY KEY,
    score_impact INT NOT NULL
);

CREATE TABLE IF NOT EXISTS AnalysisHistory (
    analysis_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_name VARCHAR(100) NOT NULL,
    user_description TEXT NOT NULL,
    detected_signals TEXT NOT NULL,
    confidence_score INT NOT NULL,
    risk_level VARCHAR(60) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS RestaurantIncidents (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_name VARCHAR(100) NOT NULL,
    issue_type VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT IGNORE INTO Restaurant VALUES
    ('Burger Hub', 4.6, 1200, 8, 5),
    ('Food Palace', 4.1, 950, 19, 11),
    ('Spicy Kitchen', 3.7, 720, 31, 20);

INSERT IGNORE INTO Reviews (restaurant_name, sentiment) VALUES
    ('Burger Hub', 'positive'), ('Burger Hub', 'positive'), ('Burger Hub', 'positive'),
    ('Food Palace', 'positive'), ('Food Palace', 'negative'),
    ('Spicy Kitchen', 'negative'), ('Spicy Kitchen', 'negative');

INSERT IGNORE INTO HygieneRules VALUES
    ('bad smell', -20), ('sour smell', -15), ('rotten smell', -25),
    ('damaged packaging', -15), ('cold food', -5), ('undercooked chicken', -45),
    ('undercooked meat', -40), ('slimy vegetables', -25), ('mold', -60),
    ('expired food', -50), ('contamination', -45), ('unusual taste', -10),
    ('stale food', -10), ('food poisoning symptoms', -50), ('improper storage', -25),
    ('raw chicken', -45), ('hair in food', -20), ('foreign object', -35),
    ('spoilage', -30), ('potential microbial growth', -30);
