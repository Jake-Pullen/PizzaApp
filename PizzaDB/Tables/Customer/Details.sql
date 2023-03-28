CREATE TABLE [customer].[details] (
  customer_id INT NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  phone_num VARCHAR(20) NOT NULL,
  street_address VARCHAR(100) NOT NULL,
  city VARCHAR(50) NOT NULL,
  postcode VARCHAR(10) NOT NULL,
  CONSTRAINT pk_customer_details PRIMARY KEY (customer_id),
);