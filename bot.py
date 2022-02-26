import discord
from discord.ext import commands
import json
import requests

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.command()
async def реклама(ctx):
    await ctx.send('**Привет! Поддержка бота: https://discord.gg/maldivcm** <a:aRASH:937281359746039818> ')

@client.command()
async def сказать(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()

@client.command()
async def хелп(ctx):
    embed = discord.Embed(
        title = '**Команды** </>',
        description = '''Привет! Меня зовут FlexinBot! Вот мои команды: 

`Модерация`
`бан`, `кик`, `warn`, `say`.

`Утилиты`
 `сказать`, `аватарка`, `user`, `server`, `cat`, `лиса`,`собака`,``,`koala`.

`Система`
`инфобот`.

**Префикс: [!]**''',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )


    await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} выгнан с гильдии. <a:aRASH:937281359746039818>")

@client.command()
@commands.has_permissions(ban_members=True)
async def бан(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} забанен на гильдии. <a:aRASH:937281359746039818>")

@client.command()
async def аватарка(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@client.command()
async def очистить(ctx, amount=None):

    await ctx.channel.purge(limit=int(amount))
    embed = discord.Embed(
        description = '<a:aRASH:937281359746039818> Успешно удалено!',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, команда не найдена \:(.**', color=0x0c0c0c))


@client.event
async def on_ready():
    activity = discord.Game(name="Префикс: ! | discord.gg/maldivcm", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Случайная лиса') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Команда выполнена: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Случайная кошка -^-') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Команда выполнена: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Случайная собака') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Команда выполнена: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def подмигнуть(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Подмигнивание') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Команда выполнена: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def сервер(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = "<@943868429004337192>"
  id = str(ctx.guild.id)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Информация о сервере",
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Владелец", value=owner, inline=True)
  embed.add_field(name="ID сервера", value=id, inline=True)
  embed.add_field(name="Количество участников", value=memberCount, inline=True)

  await ctx.send(embed=embed)

@client.command()
async def юзер(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)

@client.command()
async def инфобот(ctx):
    embed = discord.Embed(
        title = 'Что это за бот?',
        description = '''
**Название бота:** __FlexinBot__

**Создатель бота:** __943868429004337192__

**Сервер разработчика:** **[Ссылка на сервер](https://discord.gg/maldivcm)** __(кликабельно)__

**ЯП:** __Python__

Нашел баг? Пиши сюда! [Поддержка](https://vk.com/previouslayer)]
''',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )

    await ctx.send(embed=embed)

client.run(os.environ['TOKEN'])
