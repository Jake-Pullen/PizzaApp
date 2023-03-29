CREATE TABLE [order].[status]
(
	status_id INT NOT NULL,
	external_name Varchar(50) NOT NULL,
	CONSTRAINT pk_order_status PRIMARY KEY (status_id),
)
