-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para responder la pregunta use el archivo `data.csv`.
-- 
-- Cuente la cantidad de personas nacidas por año.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
u = LOAD 'data.csv' USING PigStorage(',') 
    AS (id:int, 
        firstname:CHARARRAY, 
        surname:CHARARRAY, 
        birthday:CHARARRAY, 
        color:CHARARRAY, 
        quantity:INT);
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

file = FOREACH u GENERATE GetYear(ToDate(birthday,'yyyy-MM-dd')) as year;

conteo = group file by year;
conteo1 = FOREACH conteo GENERATE group as year, COUNT(file) as cnt;
resultado = FOREACH conteo1 GENERATE year, cnt;

STORE resultado INTO 'output' USING PigStorage(',');

fs -copyToLocal output output
