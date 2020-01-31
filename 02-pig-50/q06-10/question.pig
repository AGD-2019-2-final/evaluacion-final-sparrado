-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv' AS (f1: CHARARRAY, f2: CHARARRAY, f3: MAP[]);
let = FOREACH data GENERATE f1, FLATTEN(KEYSET(f3)) AS f4;
let_g= FOREACH let GENERATE f4;
grouped = GROUP let_g BY f4;
contar = FOREACH grouped GENERATE group, COUNT(let_g);
STORE contar INTO 'output' USING PigStorage(',');