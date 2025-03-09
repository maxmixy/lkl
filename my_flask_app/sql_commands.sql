
-- Checks Table
CREATE TABLE Checks (
    CheckID INT PRIMARY KEY,
    CheckNumber VARCHAR(50),
    Amount DECIMAL(10, 2),
    DateIssued DATE,
    DateCleared DATE,
    Status VARCHAR(50),
    RelatedInvoiceID INT
);


-- InvoiceForm Table
CREATE TABLE InvoiceForm (
    FormID INT PRIMARY KEY,
    InvoiceID INT,
    DateCreated DATE,
    TotalAmount DECIMAL(10, 2)
);

-- InvoiceReceipt Table
CREATE TABLE InvoiceReceipt (
    ReceiptID INT PRIMARY KEY,
    InvoiceID INT,
    DateReceived DATE,
    AmountReceived DECIMAL(10, 2)
);

-- PaymentRequest Table
CREATE TABLE PaymentRequest (
    RequestID INT PRIMARY KEY,
    InvoiceID INT,
    AmountRequested DECIMAL(10, 2),
    RequestDate DATE
);

-- PurchaseOrder Table
CREATE TABLE PurchaseOrder (
    OrderID INT PRIMARY KEY,
    SupplierID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2)
);

-- PurchaseReceiving Table
CREATE TABLE PurchaseReceiving (
    ReceivingID INT PRIMARY KEY,
    OrderID INT,
    DateReceived DATE,
    Status VARCHAR(50)
);

-- PurchaseRequests Table
CREATE TABLE PurchaseRequests (
    RequestID INT PRIMARY KEY,
    ItemID INT,
    QuantityRequested INT,
    RequestDate DATE
);
