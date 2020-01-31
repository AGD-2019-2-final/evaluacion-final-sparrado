-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Compute la cantidad de registros por cada letra de la columna 1.
-- Escriba el resultado ordenado por letra. 
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS data;
CREATE TABLE data (key STRING,
                   fecha DATE,
                   valor INT)
ROW FORMAT DELIMITED FIELDS
    TERMINATED BY '\t';

LOAD DATA LOCAL INPATH 'data.tsv'
    OVERWRITE INTO TABLE data;

CREATE TABLE word_counts
AS
    SELECT key, count(1) AS count
    FROM
        data w
GROUP BY
    key
ORDER BY
    key;

SELECT * FROM word_counts LIMIT 10;

INSERT OVERWRITE LOCAL DIRECTORY 'output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
SELECT * FROM word_counts;