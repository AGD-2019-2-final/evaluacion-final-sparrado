--
-- Pregunta
-- ===========================================================================
-- 
-- El archivo `truck_event_text_partition.csv` tiene la siguiente estructura:
-- 
--   driverId       INT
--   truckId        INT
--   eventTime      STRING
--   eventType      STRING
--   longitude      DOUBLE
--   latitude       DOUBLE
--   eventKey       STRING
--   correlationId  STRING
--   driverName     STRING
--   routeId        BIGINT
--   routeName      STRING
--   eventDate      STRING
-- 
-- Escriba un script en Pig que carge los datos y obtenga los primeros 10 
-- registros del archivo para las primeras tres columnas, y luego, ordenados 
-- por driverId, truckId, y eventTime. 
--
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba su respuesta a partir de este punto <<<
-- 
data = LOAD 'truck_event_text_partition.csv' USING PigStorage(',')
       AS (f1: INT, f2: INT, f3: CHARARRAY,  f4:CHARARRAY, f5:DOUBLE, f6:DOUBLE, f7:CHARARRAY, f8:CHARARRAY, f9:CHARARRAY,        f10:INT, f11:CHARARRAY, f12:CHARARRAY));
data = LIMIT data 10;
data = ORDER data BY f1, f2, f3;
data = FOREACH data GENERATE CONCAT(f1,',', f2, ',', f3) as ld;
data = ORDER data BY ld;
STORE data INTO 'output' USING PigStorage('\t');