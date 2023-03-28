CREATE TABLE [payment].[details] (
  payment_id INT NOT NULL,
  order_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_time TIME NOT NULL,
  payment_method VARCHAR(20) NOT NULL,
  payment_amount DECIMAL(10,2) NOT NULL,
  CONSTRAINT pk_payment_details PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES [order].[details](order_id)
);