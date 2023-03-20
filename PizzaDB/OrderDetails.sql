CREATE TABLE dbo.OrderDetails (
  order_details_id INT PRIMARY KEY,
  order_id INT NOT NULL,
  pizza_type VARCHAR(50) NOT NULL,
  pizza_size VARCHAR(10) NOT NULL,
  pizza_toppings VARCHAR(100),
  pizza_crust VARCHAR(20) NOT NULL,
  pizza_quantity INT NOT NULL,
  pizza_price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);