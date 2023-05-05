CREATE TABLE [pizza].[toppings]
(
	topping_id INT NOT NULL,
	cost DECIMAL(18,2) NOT NULL,
	CONSTRAINT pk_pizza_toppings PRIMARY KEY (topping_id)
)
