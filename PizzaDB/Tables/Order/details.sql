CREATE TABLE [order].[details] (
  order_id INT NOT NULL IDENTITY(1,1),
  customer_id INT NOT NULL,
  created_date DATE NOT NULL,
  total_cost DECIMAL(10,2) NOT NULL,
  status_id INT NULL,
  CONSTRAINT pk_order_details PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES [customer].[details](customer_id)
);