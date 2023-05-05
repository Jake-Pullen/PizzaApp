CREATE PROCEDURE [order].[basket]
    @order_id INT
    ,@user_id INT
AS 
BEGIN

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
    WHERE od.customer_id = @user_id
        AND od.order_id  = @order_id
    GROUP BY os.external_name
        ,od.total_cost
END