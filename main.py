import discord

client = discord.Client()

@client.event
async def on_ready():
  print("This Bot is Online")

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.mention + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            embed_to_modmail = discord.Embed(colour = discord.Colour.green()
            )
            embed_to_modmail.set_author(name="A Message Has Come in!")
            embed_to_modmail.add_field(name="Message -", value=message.content)
            await modmail_channel.send(embed = embed_to_modmail)
            await modmail_channel.send("From - " + message.author.mention)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.mention + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]

            to_user = discord.Embed(colour = discord.Colour.red()
            )
            to_user.set_author(name="A Mod has Responded to your Message!")
            to_user.add_field(name="Message -", value=mod_message)
            await member_object.send(embed=to_user)
            await member_object.send("From - " + message.author.mention)

            l_mod = discord.embed(colour = (discord.Colour.purple()
            )
            l_mod.set_author(name="This Message has been sent :")
            l_mod.add_field(name="Message - ", value=mod_message)
            await modmail_channel.send(embed=l_mod)
            await modmail_channel.send("The Mod that wrote this message is:" + message.author.mention)
