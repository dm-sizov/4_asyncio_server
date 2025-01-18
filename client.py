import asyncio


async def send_message(message):
    reader, writer = await asyncio.open_connection('localhost', 9095)

    print(f'Send: {message}')
    writer.write(message.encode())  # Кодируем строку в байты и отправляем

    await writer.drain()  # Дожидаемся завершения отправки

    data = await reader.read(100)  # Читаем ответ от сервера
    print(f'Received: {data.decode()}')  # Декодируем и выводим ответ

    writer.close()  # Закрываем соединение


# Основная функция для запуска клиента
async def main():
    await send_message('Hello, World!')


# Запускаем программу
asyncio.run(main())
