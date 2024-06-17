SELECT
    c.CustomerID,
    c.Name AS CustomerName,
    c.Email,
    c.City,
    o.OrderID,
    o.Quantity,
    o.OrderDate,
    p.ProductID,
    p.ProductName,
    p.Price,
    i.WarehouseID,
    i.WarehouseLocation,
    i.Stock AS WarehouseStock
FROM
    order_data o
JOIN
    customer_data c ON o.CustomerID = c.CustomerID
JOIN
    product_data p ON o.ProductID = p.ProductID
LEFT JOIN
    inventory_data i ON p.ProductID = i.ProductID
