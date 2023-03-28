CREATE TABLE [pizza].[sizes]
(
	[size_id] INT NOT NULL,
	[external_name] varchar(20) NOT NULL,
	[inches] SMALLINT NOT NULL, 
	[cm] SMALLINT NOT NULL,
	CONSTRAINT pk_pizza_sizes PRIMARY KEY (size_id),
)
