﻿CREATE TABLE [order].[details] (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  order_total DECIMAL(10,2) NOT NULL,
  CONSTRAINT pk_order_details PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES [customer].[details](customer_id)
);