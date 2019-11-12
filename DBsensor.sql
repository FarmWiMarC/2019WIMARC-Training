-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 12, 2019 at 08:41 AM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id2125007_sensor`
--

-- --------------------------------------------------------

--
-- Table structure for table `a`
--

CREATE TABLE `a` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `a`
--

INSERT INTO `a` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7107, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '08:53:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7119, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7120, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `b`
--

CREATE TABLE `b` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `b`
--

INSERT INTO `b` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7107, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '08:53:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7119, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `c`
--

CREATE TABLE `c` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `c`
--

INSERT INTO `c` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7106, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:53:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7119, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `control`
--

CREATE TABLE `control` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `device` varchar(25) NOT NULL,
  `parameter` varchar(25) NOT NULL,
  `A` varchar(15) NOT NULL,
  `B` varchar(15) NOT NULL,
  `C` varchar(15) NOT NULL,
  `D` varchar(15) NOT NULL,
  `E` varchar(15) NOT NULL,
  `F` varchar(15) NOT NULL,
  `G` varchar(15) NOT NULL,
  `H` varchar(15) NOT NULL,
  `updatecode` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `controltimer`
--

CREATE TABLE `controltimer` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `d`
--

CREATE TABLE `d` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `d`
--

INSERT INTO `d` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7105, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:53:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7119, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL,
  `status` varchar(15) NOT NULL,
  `device` varchar(25) NOT NULL,
  `RESET` varchar(5) NOT NULL,
  `updatecode` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `e`
--

CREATE TABLE `e` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `e`
--

INSERT INTO `e` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7105, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `f`
--

CREATE TABLE `f` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `f`
--

INSERT INTO `f` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7104, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7105, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `g`
--

CREATE TABLE `g` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `g`
--

INSERT INTO `g` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7104, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7105, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `h`
--

CREATE TABLE `h` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h`
--

INSERT INTO `h` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7105, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `humid`
--

CREATE TABLE `humid` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `i`
--

CREATE TABLE `i` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `i`
--

INSERT INTO `i` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7105, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7114, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7115, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7116, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7117, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7118, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `j`
--

CREATE TABLE `j` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `j`
--

INSERT INTO `j` (`id`, `date`, `time`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) VALUES
(7102, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7103, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7104, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7105, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7106, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7107, '2019-11-11 ', '08:57:02 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7108, '2019-11-11 ', '09:00:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7109, '2019-11-11 ', '09:03:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7110, '2019-11-11 ', '09:06:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7111, '2019-11-11 ', '09:09:08 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7112, '2019-11-11 ', '09:12:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7113, '2019-11-11 ', '09:15:00 ', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `level`
--

CREATE TABLE `level` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `lux`
--

CREATE TABLE `lux` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `UserID` int(3) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `LoginStatus` int(1) NOT NULL,
  `LastUpdate` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `moisture`
--

CREATE TABLE `moisture` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mpibmkj1`
--

CREATE TABLE `mpibmkj1` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `Temp` varchar(5) NOT NULL,
  `Humid` varchar(5) NOT NULL,
  `Rain` varchar(5) NOT NULL,
  `WindS` varchar(5) NOT NULL,
  `WindD` varchar(5) NOT NULL,
  `M1` varchar(5) NOT NULL,
  `M2` varchar(5) NOT NULL,
  `Lux` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rain`
--

CREATE TABLE `rain` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sensor`
--

CREATE TABLE `sensor` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `Temp` varchar(15) NOT NULL,
  `Humid` varchar(15) NOT NULL,
  `Rain` varchar(15) NOT NULL,
  `WindS` varchar(15) NOT NULL,
  `WindD` varchar(15) NOT NULL,
  `M1` varchar(15) NOT NULL,
  `M2` varchar(15) NOT NULL,
  `Lux` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`id`, `date`, `time`, `Temp`, `Humid`, `Rain`, `WindS`, `WindD`, `M1`, `M2`, `Lux`) VALUES
(7044, '2019-11-07 ', '13:29:09 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7045, '2019-11-11 ', '08:43:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7046, '2019-11-11 ', '08:48:24 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7047, '2019-11-11 ', '08:49:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7048, '2019-11-11 ', '08:50:16 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7049, '2019-11-11 ', '08:51:01 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7050, '2019-11-11 ', '08:52:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7051, '2019-11-11 ', '08:53:00 ', '0', '0', '0', '0', '0', '0', '0', '0'),
(7052, '2019-11-11 ', '08:57:02 ', '28.87', '100.00', '0.00', '362', '0.00', '663', '0', '5.80'),
(7053, '2019-11-11 ', '09:00:01 ', '29.02', '100.00', '0.00', '362', '0.00', '663', '0', '6.00'),
(7054, '2019-11-11 ', '09:03:00 ', '29.07', '100.00', '0.00', '362', '0.00', '664', '0', '6.20'),
(7055, '2019-11-11 ', '09:06:01 ', '29.33', '100.00', '0.00', '362', '0.00', '661', '0', '6.20'),
(7056, '2019-11-11 ', '09:09:08 ', '29.79', '100.00', '0.00', '362', '0.00', '661', '0', '6.50'),
(7057, '2019-11-11 ', '09:12:01 ', '29.79', '100.00', '0.00', '362', '0.00', '663', '0', '6.60'),
(7058, '2019-11-11 ', '09:15:00 ', '30.00', '100.00', '0.00', '362', '0.00', '664', '0', '6.70');

-- --------------------------------------------------------

--
-- Table structure for table `sensortest`
--

CREATE TABLE `sensortest` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `Temp` varchar(5) NOT NULL,
  `Humid` varchar(5) NOT NULL,
  `Rain` varchar(5) NOT NULL,
  `WindD` varchar(5) NOT NULL,
  `WindS` varchar(5) NOT NULL,
  `Lux` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL,
  `I` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `setdevice`
--

CREATE TABLE `setdevice` (
  `device` varchar(100) NOT NULL,
  `parameter` varchar(25) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `Temp` varchar(25) NOT NULL,
  `Humid` varchar(25) NOT NULL,
  `Rain` varchar(25) NOT NULL,
  `WindS` varchar(25) NOT NULL,
  `WindD` varchar(25) NOT NULL,
  `M1` varchar(25) NOT NULL,
  `M2` varchar(25) NOT NULL,
  `Lux` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `setsensor`
--

CREATE TABLE `setsensor` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `Temp` varchar(5) NOT NULL,
  `Humid` varchar(5) NOT NULL,
  `Rain` varchar(5) NOT NULL,
  `WindS` varchar(5) NOT NULL,
  `WindD` varchar(5) NOT NULL,
  `M1` varchar(5) NOT NULL,
  `M2` varchar(5) NOT NULL,
  `Lux` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `temp`
--

CREATE TABLE `temp` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `volt`
--

CREATE TABLE `volt` (
  `id` int(11) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wind`
--

CREATE TABLE `wind` (
  `date` varchar(25) NOT NULL,
  `time` varchar(15) NOT NULL,
  `A` varchar(5) NOT NULL,
  `B` varchar(5) NOT NULL,
  `C` varchar(5) NOT NULL,
  `D` varchar(5) NOT NULL,
  `E` varchar(5) NOT NULL,
  `F` varchar(5) NOT NULL,
  `G` varchar(5) NOT NULL,
  `H` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `a`
--
ALTER TABLE `a`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `b`
--
ALTER TABLE `b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `c`
--
ALTER TABLE `c`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `d`
--
ALTER TABLE `d`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `e`
--
ALTER TABLE `e`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `f`
--
ALTER TABLE `f`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `g`
--
ALTER TABLE `g`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `h`
--
ALTER TABLE `h`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `i`
--
ALTER TABLE `i`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `j`
--
ALTER TABLE `j`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `volt`
--
ALTER TABLE `volt`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `a`
--
ALTER TABLE `a`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7121;

--
-- AUTO_INCREMENT for table `b`
--
ALTER TABLE `b`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7120;

--
-- AUTO_INCREMENT for table `c`
--
ALTER TABLE `c`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7120;

--
-- AUTO_INCREMENT for table `d`
--
ALTER TABLE `d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7120;

--
-- AUTO_INCREMENT for table `e`
--
ALTER TABLE `e`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7119;

--
-- AUTO_INCREMENT for table `f`
--
ALTER TABLE `f`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7118;

--
-- AUTO_INCREMENT for table `g`
--
ALTER TABLE `g`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7118;

--
-- AUTO_INCREMENT for table `h`
--
ALTER TABLE `h`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7118;

--
-- AUTO_INCREMENT for table `i`
--
ALTER TABLE `i`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7119;

--
-- AUTO_INCREMENT for table `j`
--
ALTER TABLE `j`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7114;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `UserID` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7059;

--
-- AUTO_INCREMENT for table `volt`
--
ALTER TABLE `volt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7105;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
