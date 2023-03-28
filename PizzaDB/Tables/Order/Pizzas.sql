CREATE TABLE [order].[pizzas] (
  order_pizza_id INT NOT NULL,
  order_id INT NOT NULL,
  pizza_template_id INT NULL,
  is_custom BIT NOT NULL DEFAULT 0,
  CONSTRAINT pk_order_pizzas PRIMARY KEY (order_pizza_id),
  FOREIGN KEY (order_id) REFERENCES [order].[details](order_id),
  FOREIGN KEY (pizza_template_id) REFERENCES [pizza].[templates](template_id)
);