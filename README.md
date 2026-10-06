## Project Description

This project demonstrates an end-to-end E-commerce Data Engineering pipeline that extracts data from SQL Server, transforms and validates it using Python/Pandas, and loads it into Snowflake.

The pipeline supports incremental data processing using SQL Server Change Tracking and watermark management, with Snowflake MERGE, Streams and Tasks used to process INSERT, UPDATE and DELETE changes. Logging, configuration management and exception handling are also implemented for reliable ETL execution.
