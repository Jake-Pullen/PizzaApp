-- CREATE PROCEDURE [order].[basket]
--     @order_id INT
--     ,@user_id INT
-- AS 
-- BEGIN

    SELECT 
        od.total_cost
        ,os.external_name AS order_status
        ,COUNT(op.order_pizza_id) AS pizza_count
    FROM [order].[details] AS od 
    INNER JOIN [order].[pizzas] AS op
        ON op.order_id = od.order_id
    INNER JOIN pizza.sizes AS ps 
        ON ps.size_id = op.pizza_size_id
    LEFT OUTER JOIN [order].[status] AS os 
        ON od.status_id = os.status_id
    WHERE od.customer_id = 1 -- @user_id
        AND od.order_id  = 1 -- @order_id
    GROUP BY os.external_name
        ,od.total_cost
-- END

    DECLARE @ADD_COST DECIMAL(10,2) = (
    SELECT ps.cost + SUM(pt.cost) AS add_cost
    FROM [order].[details] AS od 
    INNER JOIN [order].[pizzas] AS op
        ON op.order_id = od.order_id
    INNER JOIN pizza.sizes AS ps 
        ON ps.size_id = op.pizza_size_id
    INNER JOIN  [order].[pizza_toppings] AS opt 
        ON opt.order_pizza_id = op.order_pizza_id
    INNER JOIN pizza.toppings AS pt 
        ON pt.topping_id = opt.topping_id
    WHERE op.order_pizza_id = 2
    GROUP BY ps.cost);
    
    UPDATE od
    SET od.total_cost = od.total_cost + @add_cost
    FROM [order].[details] AS od 
    INNER JOIN [order].[pizzas] AS op
        ON op.order_id = od.order_id
    WHERE op.order_pizza_id = 2
