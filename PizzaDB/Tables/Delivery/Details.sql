CREATE TABLE [Delivery].Details (
  order_id INT PRIMARY KEY,
  delivery_address VARCHAR(100) NOT NULL,
  delivery_driver VARCHAR(50) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES [Order].Details(order_id)
);