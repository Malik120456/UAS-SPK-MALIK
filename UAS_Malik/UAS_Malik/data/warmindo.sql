-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2023 at 12:21 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warmindo`
--

-- --------------------------------------------------------

--
-- Table structure for table `warmindo`
--

CREATE TABLE `warmindo` (
  `warmindo` varchar(50) DEFAULT NULL,
  `Harga_Minuman` int(11) DEFAULT NULL,
  `Harga_Makanan` int(11) DEFAULT NULL,
  `tahun_berdiri` int(11) DEFAULT NULL,
  `jumlah_menu` int(11) DEFAULT NULL,
  `kode` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `warmindo`
--

INSERT INTO `warmindo` (`warmindo`, `Harga_Minuman`, `Harga_Makanan`, `tahun_berdiri`, `jumlah_menu`, `kode`) VALUES
('Warmindo Uti', 8000, 12000, 2022, 33, 'A1'),
('Warmindo Sari', 8000, 11000, 2022, 29, 'A2'),
('Warmindo 99', 8000, 10000, 2022, 28, 'A3'),
('Warmindo 86', 8000, 10000, 2022, 30, 'A4'),
('Warmindo Sueb', 8000, 10000, 2022, 30, 'A5'),
('Warmindo Sami', 8000, 10000, 2023, 30, 'A6'),
('Warmindo Najib', 5000, 10000, 2023, 30, 'A7'),
('Warmindo Isti', 5000, 9000, 2023, 30, 'A8'),
('Warmindo Bundo', 5000, 9000, 2023, 30, 'A9');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
