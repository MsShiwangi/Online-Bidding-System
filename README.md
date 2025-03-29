## Online-Bidding-System
This project uses Python MySql connectivity for managing and processing real life based online bidding system.

## Features
User registration and authentication
Real-time bidding on items
Bid history tracking
Item management for administrators

## Technologies Used
Python : For internal logic and database connectivity.
MySQL: Database management system for storing user and bidding data

## Usage
Register for an account to start bidding.
Browse available items and place bids.
Monitor your bid status and receive notifications.

## Pre-requisites
Here’s a complete, step-by-step guide to help you set up and run this project from scratch.
	1.	Install MySQL: Download and install MySQL Server from here.
	2.	Install Python: If Python isn’t installed, download it from here.
	3.	Install a Code Editor: Install Visual Studio Code (VS Code) from here for easy editing and running of code.

### Step 1: Setting Up MySQL Database

	1.	Open MySQL Command Line or MySQL Workbench:
	•	Log in with your MySQL username and password.
	2.	Create the Database and Tables:
	•	Run the following commands one at a time in MySQL to set up your database and tables.

CREATE DATABASE bidding_system;
USE bidding_system;

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role ENUM('admin', 'buyer', 'seller') NOT NULL
);

CREATE TABLE Items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_id INT NOT NULL,
    description TEXT NOT NULL,
    min_bid DECIMAL(10, 2) NOT NULL,
    max_bid DECIMAL(10, 2) DEFAULT 0,
    status ENUM('open', 'closed') DEFAULT 'open',
    FOREIGN KEY (seller_id) REFERENCES Users(user_id)
);

CREATE TABLE Bids (
    bid_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    buyer_id INT NOT NULL,
    bid_amount DECIMAL(10, 2) NOT NULL,
    bid_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES Items(item_id),
    FOREIGN KEY (buyer_id) REFERENCES Users(user_id)
);


	3.	Verify Table Creation:
	•	Run SHOW TABLES; to check that Users, Items, and Bids tables have been created.

### Step 2: Setting Up Python Environment

	1.	Install MySQL Connector for Python:
	•	Open a terminal (command prompt) and run:

pip install mysql-connector-python


	2.	Create a Python File for the Project:
	•	Open your code editor (like VS Code).
	•	Create a new file, e.g., bidding_system.py.
	3.	Paste the Python Code:
	•	Copy the provided code into bidding_system.py. This code includes functions to manage users, items, and bids.
