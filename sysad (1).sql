-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2025 at 01:03 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sysad`
--

-- --------------------------------------------------------

--
-- Table structure for table `checkissuance`
--

CREATE TABLE `checkissuance` (
  `check_number` varchar(255) NOT NULL,
  `date_cleared` date NOT NULL,
  `bank` varchar(255) NOT NULL,
  `check_date` date NOT NULL,
  `paid_to` varchar(255) NOT NULL,
  `account_no` varchar(255) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `total_applied` decimal(10,2) NOT NULL,
  `clearing_no` varchar(255) NOT NULL,
  `clearing_date` date NOT NULL,
  `company` varchar(255) NOT NULL,
  `total_gross` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `position` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `GroupID` int(11) NOT NULL,
  `InvoiceID` int(11) NOT NULL,
  `InvDate` date NOT NULL,
  `InvType` varchar(20) NOT NULL,
  `ProjID` int(11) NOT NULL,
  `CustomerID` int(11) NOT NULL,
  `AccManID` int(11) NOT NULL,
  `LeadDiv` varchar(20) NOT NULL,
  `Remarks` text NOT NULL,
  `IntTerms` int(11) NOT NULL,
  `CusTerms` int(11) NOT NULL,
  `PaymentType` varchar(20) NOT NULL,
  `ItemID` int(11) NOT NULL,
  `TPCContact` text NOT NULL,
  `TPCGross` float NOT NULL,
  `Gross` float NOT NULL,
  `Returns` float NOT NULL,
  `Payment` float NOT NULL,
  `Debit` float NOT NULL,
  `Credit` float NOT NULL,
  `Balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`GroupID`, `InvoiceID`, `InvDate`, `InvType`, `ProjID`, `CustomerID`, `AccManID`, `LeadDiv`, `Remarks`, `IntTerms`, `CusTerms`, `PaymentType`, `ItemID`, `TPCContact`, `TPCGross`, `Gross`, `Returns`, `Payment`, `Debit`, `Credit`, `Balance`) VALUES
(1, 101, '2023-01-01', 'Sale', 1, 1, 1, 'Division A', 'First invoice for Popmart Toy A', 30, 30, 'Credit Card', 1, 'Contact A', 150, 150, 0, 150, 0, 150, 0),
(1, 102, '2023-01-02', 'Sale', 1, 2, 1, 'Division B', 'Second invoice for Popmart Toy B', 30, 30, 'Credit Card', 2, 'Contact B', 250, 250, 0, 250, 0, 250, 0),
(1, 103, '2023-01-03', 'Sale', 1, 3, 1, 'Division C', 'Third invoice for Popmart Toy C', 30, 30, 'Credit Card', 3, 'Contact C', 350, 350, 0, 350, 0, 350, 0),
(1, 104, '2023-01-04', 'Sale', 1, 4, 1, 'Division D', 'Fourth invoice for Popmart Toy D', 30, 30, 'Credit Card', 4, 'Contact D', 450, 450, 0, 450, 0, 450, 0),
(1, 105, '2023-01-05', 'Sale', 1, 5, 1, 'Division E', 'Fifth invoice for Popmart Toy E', 30, 30, 'Credit Card', 5, 'Contact E', 550, 550, 0, 550, 0, 550, 0),
(1, 1001, '2023-01-15', 'Standard', 101, 201, 301, 'Sales', 'First invoice', 0, 0, 'Credit', 1, 'Contact A', 1000, 1000, 0, 0, 0, 0, 1000),
(1, 1002, '2023-02-20', 'Standard', 102, 202, 302, 'Sales', 'Second invoice', 0, 0, 'Credit', 2, 'Contact B', 1500, 1500, 0, 0, 0, 0, 1500);

-- --------------------------------------------------------

--
-- Table structure for table `invoiceform`
--

CREATE TABLE `invoiceform` (
  `FormID` int(11) NOT NULL,
  `InvoiceID` int(11) DEFAULT NULL,
  `DateCreated` date DEFAULT NULL,
  `TotalAmount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoiceform`
--

INSERT INTO `invoiceform` (`FormID`, `InvoiceID`, `DateCreated`, `TotalAmount`) VALUES
(1, 1001, '2023-01-15', 1000.00),
(2, 1002, '2023-02-20', 1500.00);

-- --------------------------------------------------------

--
-- Table structure for table `invoicereceipt`
--

CREATE TABLE `invoicereceipt` (
  `ReceiptID` int(11) NOT NULL,
  `InvoiceID` int(11) DEFAULT NULL,
  `DateReceived` date DEFAULT NULL,
  `AmountReceived` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoicereceipt`
--

INSERT INTO `invoicereceipt` (`ReceiptID`, `InvoiceID`, `DateReceived`, `AmountReceived`) VALUES
(1, 1001, '2023-01-30', 1000.00),
(2, 1002, '2023-02-28', 1500.00);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `ItemID` int(11) NOT NULL,
  `ItemName` varchar(50) NOT NULL,
  `Status` varchar(20) NOT NULL,
  `Description` text NOT NULL,
  `Accepted` float NOT NULL,
  `Gross` float NOT NULL,
  `Billed` float NOT NULL,
  `Amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`ItemID`, `ItemName`, `Status`, `Description`, `Accepted`, `Gross`, `Billed`, `Amount`) VALUES
(1, 'Popmart Toy A', 'Available', 'A collectible toy from Popmart series A', 100, 150, 120, 130),
(2, 'Popmart Toy B', 'Available', 'A collectible toy from Popmart series B', 200, 250, 220, 230),
(3, 'Popmart Toy C', 'Out of Stock', 'A collectible toy from Popmart series C', 300, 350, 320, 330),
(4, 'Popmart Toy D', 'Available', 'A collectible toy from Popmart series D', 400, 450, 420, 430),
(5, 'Popmart Toy E', 'Available', 'A collectible toy from Popmart series E', 500, 550, 520, 530);

-- --------------------------------------------------------

--
-- Table structure for table `paymentrequest`
--

CREATE TABLE `paymentrequest` (
  `request_id` varchar(255) NOT NULL,
  `date` date DEFAULT NULL,
  `supplier` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `purpose` varchar(255) NOT NULL,
  `remarks` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchaseorder`
--

CREATE TABLE `purchaseorder` (
  `OrderID` int(11) NOT NULL,
  `SupplierID` int(11) DEFAULT NULL,
  `OrderDate` date DEFAULT NULL,
  `TotalAmount` decimal(10,2) DEFAULT NULL,
  `order_id` varchar(255) NOT NULL,
  `order_date` date DEFAULT NULL,
  `order_type` varchar(255) NOT NULL,
  `product_type` varchar(255) NOT NULL,
  `supplier` varchar(255) NOT NULL,
  `terms` enum('1','30','60') DEFAULT NULL,
  `order_address` varchar(255) NOT NULL,
  `currency` enum('Php','Usd','Cny') DEFAULT NULL,
  `attention` varchar(255) NOT NULL,
  `currency_rate` decimal(10,2) DEFAULT NULL,
  `delivery_instructions` text DEFAULT NULL,
  `remarks` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchaseorder`
--

INSERT INTO `purchaseorder` (`OrderID`, `SupplierID`, `OrderDate`, `TotalAmount`, `order_id`, `order_date`, `order_type`, `product_type`, `supplier`, `terms`, `order_address`, `currency`, `attention`, `currency_rate`, `delivery_instructions`, `remarks`) VALUES
(1, 401, '2023-01-10', 2000.00, '', NULL, '', '', '', NULL, '', NULL, '', NULL, NULL, NULL),
(2, 402, '2023-02-15', 3000.00, '', NULL, '', '', '', NULL, '', NULL, '', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `purchasereceiving`
--

CREATE TABLE `purchasereceiving` (
  `transactionNo` varchar(255) NOT NULL,
  `date` date DEFAULT NULL,
  `supplierCode` varchar(255) NOT NULL,
  `supplierName` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `profitCenter` varchar(255) NOT NULL,
  `receivedBy` varchar(255) NOT NULL,
  `receivedDate` date DEFAULT NULL,
  `terms` varchar(255) NOT NULL,
  `taxType` varchar(255) NOT NULL,
  `ewt` decimal(10,2) DEFAULT NULL,
  `gross` decimal(10,2) DEFAULT NULL,
  `debit` decimal(10,2) DEFAULT NULL,
  `credit` decimal(10,2) DEFAULT NULL,
  `payment` decimal(10,2) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchaserequests`
--

CREATE TABLE `purchaserequests` (
  `request_id` int(11) NOT NULL,
  `request_date` date DEFAULT NULL,
  `request_type` varchar(255) NOT NULL,
  `ref_no` varchar(255) NOT NULL,
  `requestor` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `purpose` varchar(255) NOT NULL,
  `remarks` text DEFAULT NULL,
  `request_status` enum('Pending','Approved','Rejected') DEFAULT NULL,
  `date_needed` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchaserequests`
--

INSERT INTO `purchaserequests` (`request_id`, `request_date`, `request_type`, `ref_no`, `requestor`, `department`, `purpose`, `remarks`, `request_status`, `date_needed`) VALUES
(1, '2023-10-01', 'For Project', 'REF001', 'John Doe', 'IT', 'Purchase of new laptops', 'Urgent request', 'Pending', '2023-10-15'),
(2, '2023-10-02', 'For Office', 'REF002', 'Jane Smith', 'HR', 'Office supplies', 'Standard request', 'Approved', '2023-10-20'),
(3, '2023-10-03', 'For Pool', 'REF003', 'Alice Johnson', 'Finance', 'New software licenses', 'Routine request', 'Pending', '2023-10-25'),
(4, '2023-10-04', 'For Project', 'REF004', 'Michael Green', 'IT', 'New servers', 'Urgent request', 'Pending', '2023-10-30'),
(5, '2023-10-05', 'For Office', 'REF005', 'Emily White', 'HR', 'Office furniture', 'Standard request', 'Approved', '2023-11-05'),
(6, '2023-10-06', 'For Pool', 'REF006', 'Chris Black', 'Finance', 'Financial software', 'Routine request', 'Pending', '2023-11-10'),
(7, '2023-10-07', 'For Project', 'REF007', 'Sarah Blue', 'IT', 'Project management tool', 'Urgent request', 'Pending', '2023-11-15'),
(8, '2023-10-08', 'For Office', 'REF008', 'David Yellow', 'HR', 'Stationery', 'Standard request', 'Approved', '2023-11-20'),
(9, '2023-10-09', 'For Pool', 'REF009', 'Laura Red', 'Finance', 'Accounting software', 'Routine request', 'Pending', '2023-11-25'),
(10, '2023-10-10', 'For Project', 'REF010', 'Tom Purple', 'IT', 'New computers', 'Urgent request', 'Pending', '2023-11-30');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `supplier_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` text NOT NULL,
  `attention` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`) VALUES
(1, 'john_doe'),
(2, 'jane_smith'),
(3, 'alice_johnson');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checkissuance`
--
ALTER TABLE `checkissuance`
  ADD PRIMARY KEY (`check_number`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`GroupID`,`InvoiceID`,`ItemID`);

--
-- Indexes for table `invoiceform`
--
ALTER TABLE `invoiceform`
  ADD PRIMARY KEY (`FormID`);

--
-- Indexes for table `invoicereceipt`
--
ALTER TABLE `invoicereceipt`
  ADD PRIMARY KEY (`ReceiptID`);

--
-- Indexes for table `paymentrequest`
--
ALTER TABLE `paymentrequest`
  ADD PRIMARY KEY (`request_id`);

--
-- Indexes for table `purchaseorder`
--
ALTER TABLE `purchaseorder`
  ADD PRIMARY KEY (`OrderID`);

--
-- Indexes for table `purchasereceiving`
--
ALTER TABLE `purchasereceiving`
  ADD PRIMARY KEY (`transactionNo`);

--
-- Indexes for table `purchaserequests`
--
ALTER TABLE `purchaserequests`
  ADD PRIMARY KEY (`request_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `purchaserequests`
--
ALTER TABLE `purchaserequests`
  MODIFY `request_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
