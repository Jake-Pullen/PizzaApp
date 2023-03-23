CREATE TABLE [Order].Details (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  order_total DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES [Customer].Details(customer_id)
);