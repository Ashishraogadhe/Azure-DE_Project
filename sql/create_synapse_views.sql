-- Serverless view over gold layer in Data Lake
CREATE OR ALTER VIEW dbo.vw_car_sales_monthly_brand
AS
SELECT
    year_month,
    brand,
    country,
    total_units,
    total_revenue
FROM
    OPENROWSET(
        BULK 'https://yourstorageaccount.dfs.core.windows.net/gold/car_sales/',
        FORMAT = 'DELTA'
    ) AS [g];

    SELECT * FROM dbo.vw_car_sales_monthly_brand

