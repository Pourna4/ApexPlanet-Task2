SELECT * FROM Sales;
SELECT COUNT(*) AS Total_Orders
FROM Sales;
SELECT SUM(Total_Sales) AS Total_Sales
FROM Sales;
SELECT Category,
       SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY Category
ORDER BY Total_Sales DESC;
SELECT TOP 10 Product,
       SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY Product
ORDER BY Total_Sales DESC;
SELECT City,
       SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY City
ORDER BY Total_Sales DESC;
SELECT Gender,
       AVG(Total_Sales) AS Average_Sales
FROM Sales
GROUP BY Gender;
SELECT
    DATENAME(MONTH, Order_Date) AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY DATENAME(MONTH, Order_Date),
         MONTH(Order_Date)
ORDER BY MONTH(Order_Date);
