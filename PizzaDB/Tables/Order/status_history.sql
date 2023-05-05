CREATE TABLE [order].[status_history] (
  order_id INT NOT NULL,
  date_created DATETIME NOT NULL,
  status_id INT NOT NULL,
  CONSTRAINT pk_order_status_history PRIMARY KEY (order_id,status_id),
  FOREIGN KEY (order_status_id) REFERENCES [order].[details](order_id),
  FOREIGN KEY (status_id) REFERENCES [order].[status](status_id)
);
