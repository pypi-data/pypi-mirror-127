### `botco` - Telegram bot api wrapper
### Installation
```
pip install botco
```

### Quick start
```python
from botco import Bot, Dispatcher, types
from botco.contrib.fsm import FSM

bot = Bot("token_here")
dp = Dispatcher()


@dp.message(commands="start")
def start_message(message: types.Message, bot: Bot, state: FSM):
    message.answer("Hello world!")


@dp.message()
def echo(message: types.Message):
    message.reply(message.text)
    

dp.start_polling(bot)
```
