CREATE TABLE [delivery].[details] (
  order_id INT NOT NULL,
  recipient_name VARCHAR(255),
  address_line_1 VARCHAR(255),
  address_line_2 VARCHAR(255),
  city VARCHAR(255),
  county VARCHAR(255),
  postcode VARCHAR(10),
  country VARCHAR(255)
  CONSTRAINT pk_delivery_details PRIMARY KEY (order_id),
  FOREIGN KEY (order_id) REFERENCES [order].[details](order_id)
);