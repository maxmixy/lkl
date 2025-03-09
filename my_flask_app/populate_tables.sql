-- SQL Commands to Populate Tables with Sample Data

-- Insert Users
INSERT INTO Users (username) VALUES 
('john_doe'),
('jane_smith'),
('alice_johnson');

-- Insert Invoices
INSERT INTO invoice (GroupID, InvoiceID, InvDate, InvType, ProjID, CustomerID, AccManID, LeadDiv, Remarks, IntTerms, CusTerms, PaymentType, ItemID, TPCContact, TPCGross, Gross, Returns, Payment, Debit, Credit, Balance) VALUES 
(1, 1001, '2023-01-15', 'Standard', 101, 201, 301, 'Sales', 'First invoice', 'Net 30', 'Net 30', 'Credit', 1, 'Contact A', 1000.00, 1000.00, 0.00, 0.00, 0.00, 0.00, 1000.00),
(1, 1002, '2023-02-20', 'Standard', 102, 202, 302, 'Sales', 'Second invoice', 'Net 30', 'Net 30', 'Credit', 2, 'Contact B', 1500.00, 1500.00, 0.00, 0.00, 0.00, 0.00, 1500.00);

-- Insert Items
INSERT INTO Items (ItemID, ItemName, Status, Description, Accepted, Gross, Billed, Amount) VALUES 
(1, 'Item A', 'Available', 'Description for Item A', TRUE, 500.00, 500.00, 500.00),
(2, 'Item B', 'Available', 'Description for Item B', TRUE, 750.00, 750.00, 750.00);

-- Insert Checks
INSERT INTO Checks (CheckID, CheckNumber, Amount, DateIssued, DateCleared, Status, RelatedInvoiceID) VALUES 
(1, 'CHK001', 1000.00, '2023-01-20', '2023-01-25', 'Cleared', 1001),
(2, 'CHK002', 1500.00, '2023-02-25', NULL, 'Pending', 1002);

-- Insert Disbursement
INSERT INTO Disbursement (DisbursementID, Amount, Date, Status, RelatedInvoiceID) VALUES 
(1, 500.00, '2023-01-22', 'Completed', 1001),
(2, 750.00, '2023-02-28', 'Pending', 1002);

-- Insert InvoiceForm
INSERT INTO InvoiceForm (FormID, InvoiceID, DateCreated, TotalAmount) VALUES 
(1, 1001, '2023-01-15', 1000.00),
(2, 1002, '2023-02-20', 1500.00);

-- Insert InvoiceReceipt
INSERT INTO InvoiceReceipt (ReceiptID, InvoiceID, DateReceived, AmountReceived) VALUES 
(1, 1001, '2023-01-30', 1000.00),
(2, 1002, '2023-02-28', 1500.00);

-- Insert PaymentRequest
INSERT INTO PaymentRequest (RequestID, InvoiceID, AmountRequested, RequestDate) VALUES 
(1, 1001, 1000.00, '2023-01-15'),
(2, 1002, 1500.00, '2023-02-20');

-- Insert PurchaseOrder
INSERT INTO PurchaseOrder (OrderID, SupplierID, OrderDate, TotalAmount) VALUES 
(1, 401, '2023-01-10', 2000.00),
(2, 402, '2023-02-15', 3000.00);

-- Insert PurchaseReceiving
INSERT INTO PurchaseReceiving (ReceivingID, OrderID, DateReceived, Status) VALUES 
(1, 1, '2023-01-12', 'Received'),
(2, 2, '2023-02-18', 'Pending');

-- Insert PurchaseRequests
INSERT INTO PurchaseRequests (RequestID, ItemID, QuantityRequested, RequestDate) VALUES 
(1, 1, 10, '2023-01-05'),
(2, 2, 5, '2023-02-10');

-- Insert Purchasing
INSERT INTO Purchasing (PurchaseID, SupplierID, TotalAmount, PurchaseDate) VALUES 
(1, 401, 2000.00, '2023-01-10'),
(2, 402, 3000.00, '2023-02-15');

-- Insert Tabs
INSERT INTO Tabs (TabID, TabName, RelatedEntityID) VALUES 
(1, 'Tab 1', 1001),
(2, 'Tab 2', 1002);
