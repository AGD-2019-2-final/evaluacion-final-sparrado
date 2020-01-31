-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

data = LOAD 'data.tsv' AS (f1: CHARARRAY, f2: CHARARRAY, f3: INT);
data = ORDER data BY f3;
data = FOREACH data GENERATE f3;
data = LIMIT data 5;
STORE data INTO 'output';