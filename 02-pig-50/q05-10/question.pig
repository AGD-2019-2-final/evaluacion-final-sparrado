-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

data = LOAD 'data.tsv' AS (f1: CHARARRAY, f2: BAG{t:(p:CHARARRAY)});
let = FOREACH data GENERATE f1, FLATTEN(f2);
let_g= FOREACH let GENERATE p;
grouped = GROUP let_g BY p;
contar = FOREACH grouped GENERATE group, COUNT(let_g);
STORE contar INTO 'output';