CREATE TABLE [pizza].[templates]
(
	template_id INT NOT NULL,
	external_name VARCHAR(100) NULL,
	CONSTRAINT pk_pizza_templates PRIMARY KEY (template_id)
)
