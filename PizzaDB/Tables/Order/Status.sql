CREATE TABLE [Order].[Status] (
  orderstatus_id INT PRIMARY KEY,
  orderstatus_date DATE NOT NULL,
  orderstatus_time TIME NOT NULL,
  orderstatus_status VARCHAR(20) NOT NULL
  FOREIGN KEY (orderstatus_id) REFERENCES [Order].Details(order_id)
);
