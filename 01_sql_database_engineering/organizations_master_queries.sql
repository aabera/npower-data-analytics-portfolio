-- =====================================================================
-- 🛠️ MICROSOFT SQL SERVER (T-SQL) MASTER CHEAT SHEET
-- =====================================================================

-- 1. DATABASE & TABLE NAVIGATION
USE ashdb;

-- List all tables in the active database
SELECT name FROM sys.tables;

-- Inspect columns and properties of a specific table
EXEC sp_help 'organizations-100';


-- 2. QUERYING, SORTING & PATTERN MATCHING
SELECT * FROM [organizations-100];

-- Filter and sort: View top 10 largest companies
SELECT TOP 10 Name, Country, Number_of_employees 
FROM [organizations-100]
ORDER BY Number_of_employees DESC;

-- Text pattern searching using the LIKE wildcard (%)
SELECT Name, Country, Industry
FROM [organizations-100]
WHERE Name LIKE '%Group%' OR Name LIKE '%Inc%';


-- 3. SUMMARIZING DATA (AGGREGATIONS & GROUPING)
SELECT 
    Country,
    COUNT(*) AS Total_Companies,
    AVG(Number_of_employees) AS Avg_Employees,
    MAX(Number_of_employees) AS Max_Employees
FROM [organizations-100]
GROUP BY Country
ORDER BY Country ASC;

-- Filter aggregated rows using HAVING
SELECT 
    Country,
    COUNT(*) AS Total_Companies
FROM [organizations-100]
GROUP BY Country
HAVING COUNT(*) > 1
ORDER BY Total_Companies DESC;


-- 4. RELATIONAL JOINS
-- INNER JOIN: Merges rows where IDs match in BOTH tables
SELECT 
    org.Name, org.Country, fin.Annual_Revenue_USD, fin.Profit_Margin_Pct
FROM [organizations-100] AS org
INNER JOIN [organization-financials] AS fin 
    ON org.Organization_Id = fin.Organization_Id;

-- LEFT JOIN: Preserves all rows from the left table, filling missing right data with NULL
SELECT 
    org.Name, org.Country, fin.Annual_Revenue_USD
FROM [organizations-100] AS org
LEFT JOIN [organization-financials] AS fin 
    ON org.Organization_Id = fin.Organization_Id
ORDER BY fin.Annual_Revenue_USD DESC;
