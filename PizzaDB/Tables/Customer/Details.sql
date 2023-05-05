CREATE TABLE [customer].[details] (
  customer_id INT NOT NULL IDENTITY(1,1),
  email VARCHAR(128) NULL,
  full_name VARCHAR(100) NULL,
  phone_num VARCHAR(20) NULL,
  street_address VARCHAR(100) NULL,
  city VARCHAR(50) NULL,
  postcode VARCHAR(10) NULL,
  password_hash NVARCHAR(MAX) NULL
  CONSTRAINT pk_customer_details PRIMARY KEY (customer_id),
  CONSTRAINT uc_customer_email UNIQUE (email),

);