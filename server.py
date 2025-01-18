import asyncio

# Определяем адрес и порт, на которых будет работать наш сервер
HOST = 'localhost'  # Хост, на котором будет запущен сервер
PORT = 9095  # Порт, на котором будет слушать сервер


# Асинхронная функция для обработки входящих соединений
async def handle_echo(reader, writer):
    # Чтение данных от клиента (до 100 байт)
    data = await reader.read(100)
    message = data.decode()  # Декодируем байты в строку

    # Для демонстрации выводим полученное сообщение в консоль
    print(f"Received: {message}")

    # Отправка обратно то же самое сообщение (эхо)
    writer.write(data)  # Отправляем данные обратно клиенту
    await writer.drain()  # Дожидаемся завершения отправки

    # Закрытие соединения с клиентом
    writer.close()  # Закрываем поток записи


# Создаем цикл событий и запускаем сервер
async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)

    # Информация о запуске сервера
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # Запускаем обработку входящих запросов до тех пор, пока сервер не будет остановлен
    async with server:
        await server.serve_forever()

# Запускаем программу
asyncio.run(main())
