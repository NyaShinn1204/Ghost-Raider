import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
        if message.content == "!join":
            if message.author.voice is None:
                await message.channel.send("あなたはボイスチャンネルに接続していません。")
                return
            # ボイスチャンネルに接続する
            await message.author.voice.channel.connect()
            await message.channel.send("接続しました。")
    
        elif message.content == "!leave":
            if message.guild.voice_client is None:
                await message.channel.send("接続していません。")
                return
    
            # 切断する
            await message.guild.voice_client.disconnect()
    
            await message.channel.send("切断しました。")
        if message.content == "!wakka":
            if message.guild.voice_client is None:
                await message.channel.send("接続していません。")
                return
            message.guild.voice_client.play(discord.FFmpegPCMAudio("oto.mp3"))
            await message.channel.send("再生中...")
        if message.content == "!punchrusia":
            if message.guild.voice_client is None:
                await message.channel.send("接続していません。")
                return
            message.guild.voice_client.play(discord.FFmpegPCMAudio("rushia.mp3"))
            await message.channel.send("再生中...")
            
        if message.content == 'songlist':
            await message.channel.send('おとわっか\nるしあなぐる')
                
client = MyClient()
client.run('MTA4NDM2Njc4OTU0MDA1NzE1OQ.G2VlPr.WtNtakb1JgquTfOEoS0AHttX4e8KyYG7q17H3c')