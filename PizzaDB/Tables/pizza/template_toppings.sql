CREATE TABLE [pizza].[template_toppings]
(
	template_id INT NOT NULL,
	topping_id INT NOT NULL, 
    CONSTRAINT pk_pizza_template_toppings PRIMARY KEY (template_id,topping_id),
	FOREIGN KEY (template_id) REFERENCES [pizza].[templates](template_id),
	FOREIGN KEY (topping_id) REFERENCES [pizza].[toppings](topping_id)
)
