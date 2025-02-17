-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2025 at 06:26 PM
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
(1, 105, '2023-01-05', 'Sale', 1, 5, 1, 'Division E', 'Fifth invoice for Popmart Toy E', 30, 30, 'Credit Card', 5, 'Contact E', 550, 550, 0, 550, 0, 550, 0);

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
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`GroupID`,`InvoiceID`,`ItemID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
