# Bavera

[![PyPI](https://img.shields.io/pypi/l/bavera.svg)](https://pypi.python.org/pypi/bavera/)
[![PyPI](https://img.shields.io/pypi/v/bavera.svg)](https://pypi.python.org/pypi/bavera/)
[![TravisCI](https://img.shields.io/travis/bavera/bavera.svg)](https://travis-ci.org/bavera/bavera/)

Bavera is an extensive and extendable Python 3.x library for the [Discord API](https://discord.com/developers/docs/intro). Bavera boasts the following major features:

- Expressive, functional interface that gets out of the way
- Built for high-performance and efficiency
- Configurable and modular, take the bits you need
- Full support for Python 3.x
- Evented networking and IO using Gevent

## Installation

Bavera was built to run both as a generic-use library, and a standalone bot toolkit. Installing bavera is as easy as running `pip install bavera`, however some extra packages are recommended for power-users, namely:

|Name|Reason|
|----|------|
|requests[security]|adds packages for a proper SSL implementation|
|ujson|faster json parser, improves performance|
|erlpack (2.x), earl-etf (3.x)|ETF parser run with the --encoder=etf flag|
|gipc|Gevent IPC, required for autosharding|

## Examples

Simple bot using the builtin bot authoring tools:

```python
from bavera.bot import Bot, Plugin


class SimplePlugin(Plugin):
    # Plugins provide an easy interface for listening to Discord events
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        event.channel.send_message('Woah, a new channel huh!')

    # They also provide an easy-to-use command component
    @Plugin.command('ping')
    def on_ping_command(self, event):
        event.msg.reply('Pong!')

    # Which includes command argument parsing
    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)
```

Using the default bot configuration, we can now run this script like so:

`python -m bavera.cli --token="MY_DISCORD_TOKEN" --run-bot --plugin simpleplugin`

And commands can be triggered by mentioning the bot (configured by the BotConfig.command\_require\_mention flag):

![](http://i.imgur.com/Vw6T8bi.png)
