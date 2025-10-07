CREATE DATABASE IF NOT EXISTS `universidad` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `universidad`;

-- Tabla alumno
DROP TABLE IF EXISTS `alumno`;
CREATE TABLE `alumno` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idAlumno`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla alumno_materia
DROP TABLE IF EXISTS `alumno_materia`;
CREATE TABLE `alumno_materia` (
  `IdAlumno` int NOT NULL,
  `idMateria` int NOT NULL,
  PRIMARY KEY (`IdAlumno`,`idMateria`),
  KEY `FK_idMateria_idx` (`idMateria`),
  CONSTRAINT `Fk_Alumno` FOREIGN KEY (`IdAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `FK_MATERIA` FOREIGN KEY (`idMateria`) REFERENCES `materia` (`idMateria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla calificacion
DROP TABLE IF EXISTS `calificacion`;
CREATE TABLE `calificacion` (
  `idCalificacion` int NOT NULL AUTO_INCREMENT,
  `Nota` varchar(45) DEFAULT NULL,
  `Fecha` varchar(45) DEFAULT NULL,
  `Tipo` varchar(45) DEFAULT NULL,
  `idMateria` int DEFAULT NULL,
  `idAlumno` int DEFAULT NULL,
  PRIMARY KEY (`idCalificacion`),
  KEY `FK_idMateria_idx` (`idMateria`),
  KEY `FK_idAlumno_idx` (`idAlumno`),
  CONSTRAINT `FK_idAlumno` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `FK_idMateria` FOREIGN KEY (`idMateria`) REFERENCES `materia` (`idMateria`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla carrera
DROP TABLE IF EXISTS `carrera`;
CREATE TABLE `carrera` (
  `idCarrera` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCarrera`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla catedratico
DROP TABLE IF EXISTS `catedratico`;
CREATE TABLE `catedratico` (
  `idCatedratico` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCatedratico`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla materia
DROP TABLE IF EXISTS `materia`;
CREATE TABLE `materia` (
  `idMateria` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `idSemestre` int DEFAULT NULL,
  `idCatedratico` int DEFAULT NULL,
  PRIMARY KEY (`idMateria`),
  KEY `FK_idSemestre_idx` (`idSemestre`),
  KEY `Fk_idCatedratico_idx` (`idCatedratico`),
  CONSTRAINT `Fk_idCatedratico` FOREIGN KEY (`idCatedratico`) REFERENCES `catedratico` (`idCatedratico`),
  CONSTRAINT `FK_idSemestre` FOREIGN KEY (`idSemestre`) REFERENCES `semestre` (`idSemestre`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla semestre
DROP TABLE IF EXISTS `semestre`;
CREATE TABLE `semestre` (
  `idSemestre` int NOT NULL AUTO_INCREMENT,
  `Fecha` varchar(45) DEFAULT NULL,
  `idCarrera` int DEFAULT NULL,
  PRIMARY KEY (`idSemestre`),
  KEY `FK_idCarrera_idx` (`idCarrera`),
  CONSTRAINT `FK_idCarrera` FOREIGN KEY (`idCarrera`) REFERENCES `carrera` (`idCarrera`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;