CREATE TABLE dbo.Orders (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  order_total DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES dbo.Customers(customer_id)
);