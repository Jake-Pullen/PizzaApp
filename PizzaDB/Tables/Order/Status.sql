CREATE TABLE [order].[status] (
  orderstatus_id INT PRIMARY KEY,
  orderstatus_date DATE NOT NULL,
  orderstatus_time TIME NOT NULL,
  orderstatus_status VARCHAR(20) NOT NULL
  FOREIGN KEY (orderstatus_id) REFERENCES [order].details(order_id)
);
