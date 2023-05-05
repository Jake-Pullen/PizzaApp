CREATE PROCEDURE [order].[basket_items]
    @order_id INT
    ,@user_id INT
AS 
BEGIN

    SELECT 
         op.order_pizza_id
        ,ps.external_name AS pizza_size
        ,STRING_AGG(pt.topping_name,', ') AS toppings
		,SUM(pt.cost) + ps.cost AS pizza_cost
    FROM [order].[details] AS od 
    INNER JOIN [order].[pizzas] AS op
        ON op.order_id = od.order_id
    INNER JOIN pizza.sizes AS ps 
        ON ps.size_id = op.pizza_size_id
    INNER JOIN  [order].[pizza_toppings] AS opt 
        ON opt.order_pizza_id = op.order_pizza_id
    INNER JOIN pizza.toppings AS pt 
        ON pt.topping_id = opt.topping_id
    WHERE od.customer_id = @user_id
        AND od.order_id  = @order_id
    GROUP BY od.status_id
        ,op.order_pizza_id
        ,ps.external_name
        ,od.total_cost
		,ps.cost
END