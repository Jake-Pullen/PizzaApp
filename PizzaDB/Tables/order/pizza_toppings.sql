CREATE TABLE [order].[pizza_toppings]
(
	order_pizza_id INT NOT NULL,
	topping_id INT NOT NULL, 
    CONSTRAINT pk_order_pizza_toppings PRIMARY KEY (order_pizza_id,topping_id),
	FOREIGN KEY (order_pizza_id) REFERENCES [order].pizzas(order_pizza_id),
	FOREIGN KEY (topping_id) REFERENCES [pizza].toppings(topping_id)
)
