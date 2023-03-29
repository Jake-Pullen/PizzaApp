CREATE TABLE [delivery].[drivers]
(
  driver_id INT NOT NULL,
  driver_name VARCHAR(255) NOT NULL,
  driver_phone VARCHAR(20) NOT NULL,
  CONSTRAINT pk_delivery_drivers PRIMARY KEY (driver_id)
)
