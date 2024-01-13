--CREATE DATABASE AGO_PARCIAL
--GO
USE AGO_PARCIAL
GO
IF NOT EXISTS(SELECT * FROM SYS.TABLES WHERE OBJECT_ID=OBJECT_ID(N'DBO.DatosPersonales') AND TYPE='U')
CREATE TABLE DatosPersonales (
    DNI NCHAR(8),
    Nombre VARCHAR(255),
    EstadoCivil VARCHAR(50),
    Email VARCHAR(255),
    Telefono VARCHAR(20)
);
GO
TRUNCATE TABLE DBO.DatosPersonales
GO
BULK INSERT DatosPersonales
FROM 'C:\Users\usuario\Downloads\DATA_PERSONA.csv'
WITH (
    FIRSTROW = 2,  -- Especifica la fila en la que comienza la información de datos (en caso de que haya encabezados)
    FIELDTERMINATOR = ';',  -- Especifica el delimitador de campo (coma en este caso)
    ROWTERMINATOR = '\n',  -- Especifica el terminador de fila (nueva línea en este caso)
    TABLOCK
);

