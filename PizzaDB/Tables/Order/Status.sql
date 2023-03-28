﻿CREATE TABLE [order].[status] (
  order_status_id INT NOT NULL,
  date_created DATETIME NOT NULL,
  status_id INT NOT NULL,
  CONSTRAINT pk_order_status PRIMARY KEY (order_status_id),
  FOREIGN KEY (order_status_id) REFERENCES [order].[details](order_id)
);
