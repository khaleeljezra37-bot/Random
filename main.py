import discord
from discord.ext import commands
import aiohttp
import time

# Bot configuration
WEBSITE_URL = "https://www.logged.tg/auth/unknowngu"

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def check_website_status():
    """Check the status of the website"""
    try:
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBSITE_URL, timeout=10) as response:
                end_time = time.time()
                response_time = round((end_time - start_time) * 1000, 2)
                
                return {
                    'status': 'online',
                    'status_code': response.status,
                    'response_time': response_time
                }
    except aiohttp.ClientError as e:
        return {
            'status': 'offline',
            'error': str(e)
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e)
        }

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Monitoring: {WEBSITE_URL}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Connected to {len(bot.guilds)} server(s)')

@bot.event
async def on_message(message):
    # Debug: Print every message the bot sees
    if message.content.startswith(':'):
        print(f'Message received: {message.content} from {message.author}')
    
    # Process commands
    await bot.process_commands(message)

@bot.command(name='check', help='Check the status of the website')
async def check(ctx):
    """Check website status command"""
    result = await check_website_status()
    
    # Get user info
    user_name = ctx.author.name.lower()
    user_avatar = ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
    
    if result['status'] == 'online':
        # Create first embed for online status
        embed1 = discord.Embed(
            description=(
                "<a:fire:1451101769135427667>   ──── **WEBSITE STATUS** ────\n"
                "<a:online:1451374554369884170>  **STATUS: ONLINE**\n\n"
                "<a:inject_c:1451371999145492562> **Url:** `https://www.logged.tg/auth/unknowngu`\n"
                "<:glow:1451374133039595723>  **Response Code:** `{}` ✅\n"
                "<:glow:1451374133039595723>  **Response Time:** `{}ms`\n"
                "<a:check:1450068558477398026>  **DNS:** Resolving"
            ).format(result['status_code'], result['response_time']),
            color=0x00FF00
        )
        embed1.set_thumbnail(url="https://cdn.discordapp.com/emojis/1451374554369884170.gif")
        embed1.set_image(url="https://media.discordapp.net/attachments/1435102270416097293/1446960334861766757/a_e3816a7eb6da21f7ce5f40a2de9ff138.gif?ex=69465d13&is=69450b93&hm=f7a81fcdaa3b37ad89d8a440be0a11d44d30f004154804825bf4d467846f74f2&")
        embed1.set_footer(text=f"ᴄʜᴇᴄᴋᴇᴅ ʙʏ {user_name} 〡• ᴠɪʙᴇ ᴄʜᴇᴄᴋ™", icon_url=user_avatar)
        
        # Create second embed for online
        embed2 = discord.Embed(
            description=(
                "<a:fire:1451101769135427667>  ──── **DOMAINS STATUS** ────\n"
                "<a:online:1451374554369884170>  **STATUS: ONLINE**\n\n"
                "<a:inject_c:1451371999145492562>  **Domain:** `robiox.py`\n"
                "<:glow:1451374133039595723>  **Response Code:** `200` ✅\n"
                "<:glow:1451374133039595723>  **Response Time:** `{}ms`\n"
                "<a:check:1450068558477398026>  **DNS:** Resolving"
            ).format(result['response_time']),
            color=0x00FF00
        )
        embed2.set_thumbnail(url="https://cdn.discordapp.com/emojis/1448194511426818168.gif")
        embed2.set_image(url="https://media.discordapp.net/attachments/1435102270416097293/1442853767677743165/416a6258674a32733e5a0d5eb98e2a06.gif?ex=6945ed09&is=69449b89&hm=09bd2859bb7e0ba52119ebf4195dc02ba9f7b10520b4ef0b0f8ae200d908f68d&")
        embed2.set_footer(text=f"ᴄʜᴇᴄᴋᴇᴅ ʙʏ {user_name} 〡• ᴠɪʙᴇ ᴄʜᴇᴄᴋ™", icon_url=user_avatar)
        
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
    else:
        # Create first embed for offline status
        embed1 = discord.Embed(
            description=(
                "<a:black_fire:1447388171250958398>  ──── **WEBSITE STATUS** ────\n"
                "<a:wifi:1451369869395230740>  **STATUS: OFFLINE**\n\n"
                "<a:inject_c:1451371999145492562>  **URL:** `https://www.logged.tg/auth/unknowngu`\n"
                "<a:butterfly:1451371888365273209>  **Response Code:** `Error` ❌\n"
                "<a:butterfly:1451371888365273209>  **Response Time:** `N/A`\n"
                "<:crown:1451375098710986924>  **Server:** Down or Unreachable"
            ),
            color=0xFF0000
        )
        embed1.set_thumbnail(url="https://cdn.discordapp.com/emojis/1451369869395230740.gif")
        embed1.set_image(url="https://media.discordapp.net/attachments/1435102270416097293/1442976770407272689/100.webp?ex=6945b6d7&is=69446557&hm=25bbd03144250346be4a5c45ea5e21bb6a84fc19f84277e34b6291fb32e6dd5b&")
        embed1.set_footer(text=f"ᴄʜᴇᴄᴋᴇᴅ ʙʏ {user_name} 〡• ᴠɪʙᴇ ᴄʜᴇᴄᴋ™", icon_url=user_avatar)
        
        # Create second embed for offline
        embed2 = discord.Embed(
            description=(
                "<a:fire:1451101769135427667>  ──── **DOMAINS STATUS** ────\n"
                "<a:wifi:1451369869395230740>   **STATUS: OFFLINE**\n\n"
                "<a:inject_c:1451371999145492562>  **Domain:** `robiox.py`\n"
                "<:glow:1451374133039595723>  **Response Code:** `N/A` <a:dr_redX_No:1429420248683253860>\n"
                "<:glow:1451374133039595723> **Response Time:** `down`\n"
                "<a:check:1450068558477398026>  **DNS:** N/A"
            ),
            color=0xFF0000
        )
        embed2.set_thumbnail(url="https://cdn.discordapp.com/emojis/1451369869395230740.gif")
        embed2.set_image(url="https://media.discordapp.net/attachments/1409235007549083762/1409239970958540820/a_fad198916caeea541a5b3471a46750ad.gif?ex=69463f3f&is=6944edbf&hm=c44e4e138a2d21fda2a468f7b723068f4d28f8ae9f15fdd96baf4cdc90c296d8&")
        embed2.set_footer(text=f"ᴄʜᴇᴄᴋᴇᴅ ʙʏ {user_name} 〡• ᴠɪʙᴇ ᴄʜᴇᴄᴋ™", icon_url=user_avatar)
        
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    """Check bot ping"""
    latency = round(bot.latency * 1000, 2)
    
    embed = discord.Embed(
        title="🏓 Pong!",
        color=discord.Color.blue()
    )
    embed.add_field(name="Bot Latency", value=f"{latency}ms", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    # Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
    TOKEN = 'YOUR_BOT_TOKEN'
    bot.run(TOKEN)
