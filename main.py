from aiogram import Bot, Dispatcher, types
import asyncio
import logging

token = "5579517836:AAFFfH_Q3oM97vv_mY1vfwgFyFb05dR5SDE"

admin_id = 516698923

logger = logging.getLogger(__name__)

async def start_up(bot: Bot):
    await bot.send_message(admin_id, text="Бот запущен")

async def sd(bot: Bot):
    await bot.send_message(admin_id, text="Бот остановлен")


async def echo(message: types.Message):
    print("Получено сообщение " + message.text)
    await message.answer(message.text)


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")
    bots = Bot(token)
    dp = Dispatcher()  # Создаем диспатчер, с его помощью будем вызывать пуллинг и обрабатывать хэндлер

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    dp.message.register(echo)

    await dp.start_polling(bots)


if __name__ == "__main__":
    asyncio.run(start())
