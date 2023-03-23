CREATE TABLE [order].pizzas (
  order_Pizza_id INT PRIMARY KEY,
  order_id INT NOT NULL,
  pizza_template_id INT NULL
  FOREIGN KEY (order_id) REFERENCES [order].details(order_id)
);