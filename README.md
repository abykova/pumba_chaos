# pumba_chaos
лаборатория для Chaos Engineering в Docker Compose

1. простой микросервис + Redis
2. инструмент для хаос-тестирования (pumba)
3. тест

```
docker-compose up --build
```

http://localhost:5000

Ты увидишь: "Redis доступен!"

Через 10 секунд pumba внесёт задержку в Redis — ответ станет медленным или ошибочным

# Что происходит?

pumba начинает симулировать задержку (1000 мс) для сети Redis.
Flask-приложение продолжает слать ping, но Redis отвечает медленно.
Наблюдаем деградацию производительности.

# Что ещё можно сделать с Pumba?

Убить контейнер Redis
pumba kill --signal SIGKILL redis

Стресс по CPU
pumba stress --cpu 1 app

## Примеры запуска

```bash
make chaos-kill
make chaos-delay
make chaos-loss
make chaos-cpu

```
Или вручную:

```
./scripts/run_scenario.sh kill.yaml
```

# планы на развитие:

Добавить мониторинг (Prometheus + Grafana)
Поднять второй сервис и проверить отказоустойчивость
Ввести retry/backoff в клиенте
Использовать chaosblade или chaostoolkit
