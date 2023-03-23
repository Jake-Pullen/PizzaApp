CREATE TABLE [payment].details (
  payment_id INT PRIMARY KEY,
  order_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_time TIME NOT NULL,
  payment_method VARCHAR(20) NOT NULL,
  payment_amount DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES [order].details(order_id)
);