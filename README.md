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
