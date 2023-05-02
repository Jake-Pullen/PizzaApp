CREATE TABLE [pizza].[toppings]
(
	topping_id INT NOT NULL IDENTITY(1,1),
	topping_name VARCHAR(50) NOT NULL, 
	topping_category VARCHAR(20) NOT NULL,
	cost DECIMAL(18,2) NOT NULL,
	CONSTRAINT pk_pizza_toppings PRIMARY KEY (topping_id),
	CONSTRAINT uc_topping_names UNIQUE (topping_name)
)