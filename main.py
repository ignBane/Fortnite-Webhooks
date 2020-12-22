import requests, json, time

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = "WEBHOOK_URL HERE"

def aes():
    time.sleep(60)
    new = requests.get('https://benbotfn.tk/api/v1/aes').json()
    with open('Cache/aes.json', 'r') as f:
        Cached = json.load(f)

    if new["mainKey"] != Cached["mainKey"]:
        webhook = DiscordWebhook(url=webhook_url, username="Bane's Fish")
        embed = DiscordEmbed(title='Main AES Updated')
        embed.add_embed_field(name='mainKey', value=f'{new["mainKey"]}')
        embed.set_footer(text=f'Build: {new["version"]}')
        webhook.add_embed(embed)
        webhook.execute()
    with open('Cache/aes.json', 'w') as f:
        json.dump(new, f, indent=2)

    if new["dynamicKeys"] != Cached["dynamicKeys"]:
        for i in new["dynamicKeys"]:
            if not i in Cached["dynamicKeys"]:
                webhook = DiscordWebhook(url=webhook_url)
                embed = DiscordEmbed(title='New PAK encrypted')
                embed.add_embed_field(name=f'{i}', value=f'{new["dynamicKeys"][i]}')
                print(f'New Pak Encrypted\n{new["dynamicKeys"][i]}')
                embed.set_footer(text=f'Build: {new["version"]}')
                webhook.add_embed(embed)
                webhook.execute()

    with open('Cache/aes.json', 'w') as f:
        json.dump(new, f, indent=2)

def newCosmetics():
    time.sleep(60)
    new = requests.get('https://fortnite-api.com/v2/cosmetics/br/new').json()

    with open('Cache/newcosmetics.json', 'r') as f:
        Cached = json.load(f)

    if new["data"]["items"] != Cached["data"]["items"]:
        for i in new["data"]["items"]:
            if not i in Cached["data"]["items"]:
                webhook = DiscordWebhook(url=webhook_url)
                embed = DiscordEmbed(title='New Cosmetic', description=i["description"])
                embed.add_embed_field(name='Name', value=f'{i["name"]}')
                embed.add_embed_field(name='ID', value=f'{i["id"]}')
                try:
                    embed.add_embed_field(name='Set', value=f'{i["set"]["value"]}')
                    embed.add_embed_field(name='Series', value=f'{i["series"]["value"]}')
                except:
                    embed.add_embed_field(name='Set', value=f'{i["set"]}')
                    embed.add_embed_field(name='Series', value=f'{i["series"]}')
                embed.add_embed_field(name='Backend Type', value=f'{i["type"]["backendValue"]}')
                embed.add_embed_field(name='Rarity', value=f'{i["rarity"]["value"]}')
                embed.set_footer(text=f'Build: {new["data"]["build"]}')
                embed.set_thumbnail(url=i['images']['icon'])
                webhook.add_embed(embed)
                webhook.execute()

    with open('Cache/newcosmetics.json', 'w') as f:
        json.dump(new, f, indent=2)

while True:
    print("Loading AES, NewCosmetics")
    aes()
    newCosmetics()

 