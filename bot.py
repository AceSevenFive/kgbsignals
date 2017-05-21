import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
@client.event
async def on_message(message):
	if(message.content.startswith("%relay")):
		await client.send_message(message.author, "What is the message you wish to send? Note: This will transmit your username to the recipient. If you wish to send an anonymous message, wait 45 seconds and use %anonymousrelay.")
		tmp3 = await client.wait_for_message(author=message.author)
		print(message.mentions[0].id)
		tmp4 = await client.get_user_info(message.mentions[0].id)
		await client.send_message(await client.get_user_info(message.mentions[0].id), "Message from " + message.author.name + ": " + tmp3.content)
		tmp5 = client.get_channel("315852315699707905")
		print(tmp5)
		await client.send_message(tmp5, "Note: " + message.author.name + " sent a message to: " + tmp4.name + ".")
		await client.send_message(tmp5, "Content: " + tmp3.content)
		await client.send_message(message.author, "Message sent.")
	elif(message.content.startswith("%anonymousrelay")):
		await client.send_message(message.author, "What is the message you wish to send? Note: This will not transmit your username to the recipient. If you wish for the recipient to know the sender, wait 45 seconds and use %relay.")
		tmp3 = await client.wait_for_message(author=message.author)
		tmp4 = await client.get_user_info(message.mentions[0].id)
		await client.send_message(await client.get_user_info(message.mentions[0].id), "Message from an anonymous source: " + tmp3.content)
		tmp5 = client.get_channel("315852315699707905")
		await client.send_message(tmp5, "Note: " + message.author.name + " sent a message to: " + tmp4.name + ".")
		await client.send_message(tmp5, "Content: " + tmp3.content)
		await client.send_message(message.author, "Message sent.")
	elif(message.content.startswith("%test")):
		await client.send_message(message.channel, message.channel.id)
client.run("MzE1ODQ0NDA4OTU4Mzg2MTc3.DAMolQ.HQvKNIeFKlVs9fquTYej2b_AuFE")