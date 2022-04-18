# Redis HW
## Генерация данных
```
./json_generator.py
```

Сохранение данных в Redis

```
redis-cli < data.zset
redis-cli < data.hset
redis-cli < data.list
redis-cli -x SET mystr < data.json
```

## Измерение скорости записи-чтения

Запуск бенчмарка

```
redis-benchmark -q -n 100000
```

Результаты бенчмарка

```
PING_INLINE: 205338.81 requests per second, p50=0.135 msec
PING_MBULK: 217391.30 requests per second, p50=0.127 msec
SET: 215517.25 requests per second, p50=0.135 msec
GET: 218340.61 requests per second, p50=0.127 msec
INCR: 218818.39 requests per second, p50=0.127 msec
LPUSH: 217391.30 requests per second, p50=0.135 msec
RPUSH: 218340.61 requests per second, p50=0.135 msec
LPOP: 215982.72 requests per second, p50=0.135 msec
RPOP: 215053.77 requests per second, p50=0.127 msec
SADD: 218340.61 requests per second, p50=0.127 msec
HSET: 217864.92 requests per second, p50=0.135 msec
SPOP: 218818.39 requests per second, p50=0.127 msec
ZADD: 218340.61 requests per second, p50=0.135 msec
ZPOPMIN: 218340.61 requests per second, p50=0.127 msec
LPUSH (needed to benchmark LRANGE): 216919.73 requests per second, p50=0.135 msec
LRANGE_100 (first 100 elements): 96805.42 requests per second, p50=0.287 msec
LRANGE_300 (first 300 elements): 41963.91 requests per second, p50=0.631 msec
LRANGE_500 (first 500 elements): 27533.04 requests per second, p50=0.943 msec
LRANGE_600 (first 600 elements): 23304.59 requests per second, p50=1.111 msec
MSET (10 keys): 209643.61 requests per second, p50=0.191 msec
```

## Настройка кластера
Зайти в папку `redis-cluster` и выполнить:
```
docker compose up
```

## Результаты бенчмарка на кластере
Запуск бенчмарка
```
redis-benchmark -p 6370 -q -n 100000 > results.bench
```

Результаты:
```
PING_INLINE: 26588.67 requests per second, p50=1.575 msec
PING_MBULK: 25839.79 requests per second, p50=1.591 msec
SET: 24044.24 requests per second, p50=1.791 msec
GET: 26150.63 requests per second, p50=1.591 msec
INCR: 24073.18 requests per second, p50=1.751 msec
LPUSH: 23408.24 requests per second, p50=1.839 msec
RPUSH: 23441.16 requests per second, p50=1.855 msec
LPOP: 22820.63 requests per second, p50=1.855 msec
RPOP: 23089.36 requests per second, p50=1.815 msec
SADD: 25239.78 requests per second, p50=1.599 msec
HSET: 22351.36 requests per second, p50=1.863 msec
SPOP: 24189.65 requests per second, p50=1.655 msec
ZADD: 24497.80 requests per second, p50=1.655 msec
ZPOPMIN: 24931.44 requests per second, p50=1.671 msec
LPUSH (needed to benchmark LRANGE): 22476.96 requests per second, p50=1.895 msec
LRANGE_100 (first 100 elements): 18060.32 requests per second, p50=2.319 msec
LRANGE_300 (first 300 elements): 11524.72 requests per second, p50=3.951 msec
LRANGE_500 (first 500 elements): 8535.34 requests per second, p50=5.439 msec
LRANGE_600 (first 600 elements): 7461.57 requests per second, p50=6.199 msec
MSET (10 keys): 22197.56 requests per second, p50=1.943 msec
```
