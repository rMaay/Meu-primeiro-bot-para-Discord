import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!amazing':
            await message.channel.send(f'{message.author.name} You are amazing!')

client = MyClient()
client.run('OTI3NjQyNjgxODkzNjAxMjkw.YdNMkg.sClQ_xyPr42ZkHI2_ohRocuAzHU')