CREATE TABLE [Order].Pizzas (
  Order_Pizza_ID INT PRIMARY KEY,
  Order_ID INT NOT NULL,
  pizza_template_ID INT NULL
  FOREIGN KEY (Order_ID) REFERENCES [Order].Details(Order_ID)
);