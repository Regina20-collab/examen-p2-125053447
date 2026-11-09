# Examen Segundo Parcial - Pipeline de datos contenerizado
Matrícula: 125053447
Pregunta asignada (termina en 7): Top 10 productos por ingreso total (cantidad x precio_unitario).

## Cómo levantar
cp .env.example .env
python3 generar_dataset.py 125053447
docker compose up -d --build

## Ejecutar MapReduce
docker compose exec hadoop bash -c 'hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /data/input/ventas_125053447.csv -output /data/output/resultados -mapper mapper.py -reducer reducer.py -file /app/mapreduce/mapper.py -file /app/mapreduce/reducer.py'
python3 scripts/cargar_resultados.py output/resultados/part-00000
curl localhost:5000/resultados

## Comparativa de rendimiento
- Secuencial Python: 5.93 s
- MapReduce (Hadoop Streaming): X s (10:19)

Explicación: con 336 MB el secuencial suele ganar porque Hadoop tiene sobrecarga de arranque de JVM y de coordinación del job, que solo se compensa con volúmenes mucho mayores o un clúster distribuido.
