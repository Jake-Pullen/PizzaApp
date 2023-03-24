CREATE TABLE [order].pizzas (
  order_pizza_id INT PRIMARY KEY,
  order_id INT NOT NULL,
  pizza_template_id INT NULL,
  is_custom BIT NOT NULL DEFAULT 0
  FOREIGN KEY (order_id) REFERENCES [order].details(order_id)
);