/*
Post-Deployment Script Template							
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be appended to the build script.		
 Use SQLCMD syntax to include a file in the post-deployment script.			
 Example:      :r .\myfile.sql								
 Use SQLCMD syntax to reference a variable in the post-deployment script.		
 Example:      :setvar TableName MyTable							
               SELECT * FROM [$(TableName)]					
--------------------------------------------------------------------------------------
*/
-- Sample data for Customer table
INSERT INTO dbo.Customers (customer_id, full_name, phone_num, street_address, city, postcode)
VALUES
  (1, 'John Smith', '+44 20 1234 5678', '12 High Street', 'London', 'SW1A 1AA'),
  (2, 'Jane Doe', '+44 161 234 5678', '21 Park Road', 'Manchester', 'M14 5DP'),
  (3, 'Bob Johnson', '+44 121 234 5678', '14 Church Lane', 'Birmingham', 'B12 9QH'),
  (4, 'Alice Kim', '+44 141 234 5678', '7A Princess Street', 'Glasgow', 'G1 3NF'),
  (5, 'David Lee', '+44 1223 456 789', '3 Oxford Street', 'Cambridge', 'CB2 3QT'),
  (6, 'Sarah Jones', '+44 28 9012 3456', '27 Market Street', 'Belfast', 'BT1 2NA'),
  (7, 'James Brown', '+44 29 1234 5678', '39 Main Street', 'Cardiff', 'CF10 1GA'),
  (8, 'Emily Davis', '+44 117 234 5678', '5 Bridge Road', 'Bristol', 'BS1 6FU'),
  (9, 'Michael Wilson', '+44 20 3456 7890', '18 St. James Avenue', 'Leeds', 'LS17 8QT'),
  (10, 'Lucy Taylor', '+44 161 345 6789', '6 Victoria Road', 'Sheffield', 'S10 2TB'),
  (11, 'Oliver Jackson', '+44 121 345 6789', '8 Elm Street', 'Liverpool', 'L1 9DE'),
  (12, 'Grace Anderson', '+44 141 345 6789', '2 Park Lane', 'Edinburgh', 'EH1 3AR'),
  (13, 'Charlie Cooper', '+44 1223 456 789', '10 Elmwood Road', 'Reading', 'RG1 5DP'),
  (14, 'Mia Hernandez', '+44 28 3456 7890', '23 Highfield Avenue', 'Newcastle', 'NE1 7RU'),
  (15, 'Jacob Martin', '+44 29 3456 7890', '9 Maple Street', 'Brighton', 'BN1 2RU'),
  (16, 'Amelia Green', '+44 117 345 6789', '12 Oakwood Close', 'Leicester', 'LE1 6PA'),
  (17, 'Noah Smith', '+44 20 4567 8901', '45 Rose Avenue', 'London', 'SE1 8LP'),
  (18, 'Sophia Patel', '+44 161 456 7890', '17 Park Lane', 'Manchester', 'M1 2HT'),
  (19, 'Ethan Brown', '+44 121 456 7890', '6 Church Street', 'Birmingham', 'B3 2NP'),
  (20, 'Emma Wilson', '+44 141 456 7890', '14 Main Road', 'Glasgow', 'G3 7XX')

  -- Order table
INSERT INTO Orders (order_id, customer_id, order_date, order_status, payment_method, total_price)
VALUES
  (1, 1, '2022-01-05 14:30:00', 'delivered', 'credit card', 17.99),
  (2, 1, '2022-02-14 19:45:00', 'delivered', 'cash', 22.99),
  (3, 2, '2022-03-10 12:15:00', 'in progress', 'credit card', 13.99),
  (4, 3, '2022-04-01 20:00:00', 'canceled', 'credit card', 0.00),
  (5, 4, '2022-05-20 18:30:00', 'delivered', 'cash', 29.99),
  (6, 5, '2022-06-17 21:00:00', 'delivered', 'credit card', 15.99),
  (7, 5, '2022-07-08 13:00:00', 'delivered', 'cash', 18.99),
  (8, 6, '2022-08-19 19:30:00', 'in progress', 'credit card', 10.99),
  (9, 7, '2022-09-29 15:45:00', 'delivered', 'cash', 24.99),
  (10, 8, '2022-10-18 17:00:00', 'delivered', 'credit card', 12.99),
  (11, 9, '2022-11-12 22:15:00', 'in progress', 'credit card', 16.99),
  (12, 9, '2022-12-05 14:00:00', 'delivered', 'cash', 19.99),
  (13, 10, '2023-01-21 16:45:00', 'delivered', 'credit card', 14.99),
  (14, 11, '2023-02-14 19:30:00', 'delivered', 'cash', 28.99),
  (15, 12, '2023-03-03 20:15:00', 'delivered', 'credit card', 23.99),
  (16, 12, '2023-03-10 21:00:00', 'delivered', 'cash', 26.99),
  (17, 13, '2023-03-16 12:30:00', 'in progress', 'credit card', 21.99),
  (18, 14, '2023-03-19 17:45:00', 'delivered', 'cash', 31.99),
  (19, 15, '2023-03-20 18:00:00', 'in progress', 'credit card', 11.99),
  (20, 15, '2023-03-20 20:00:00', 'in progress', 'credit card', 10.99);

