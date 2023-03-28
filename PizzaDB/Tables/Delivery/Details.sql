CREATE TABLE [delivery].[details] (
  order_id INT PRIMARY KEY,
  delivery_address VARCHAR(100) NOT NULL,
  delivery_driver VARCHAR(50) NOT NULL,
  CONSTRAINT pk_delivery_details PRIMARY KEY (order_id),
  FOREIGN KEY (order_id) REFERENCES [order].[details](order_id)
);