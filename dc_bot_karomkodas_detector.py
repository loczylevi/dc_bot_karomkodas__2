import discord
#import os
import random
#from keep_alive import keep_alive
import os
#titkos_cuccmok = os.environ['TOKEN']
client = discord.Client()


karomkodasok = ["anyád","kurwa","kurva","geci","fasz","punci","rák","faszom","kuss","bazdmeg","kushadj","pöcs","faszomnak a genyves tövébe,","pofád","fogd be","fuck","wtf","bitch","fuck you","szétbaszom","szétbaszlak","wazze","szar","holy fuck","pöcsfej","dug","megduglak","megbaszlak","bassza","basszameg","buzi","leszbi","buzeráns","nyomorék","fogyaték","retard","retárd","fogyatékos","megdug","f@sz","b@zdmeg","baszki","basszus","kúrva","kúrwa","baszus","beszart","fasza","lofasz","lófasz","szopjál","szopjal","szopjál le","szopjal le","odabasz","baszo","basz","baszik","odabassz","fika","pina","punci","kuki","nuna","fos","foss","suna","segg","ass","redva","kur","kúr","picsa","kula","dako","dákó","dáko","ass","asshole","gec","gecc","dickhead","szemétláda","apádfaszát","shitbag","pofád","pofádlapos","nigger","niga","feka","istenfasza","anyádfasza","picsája","witch","shit","dogshit",]
tank = ["tank","panzer","tartály","páncélos","harckocsi","lánctalpas","harcjármű","ágyú","páncél","gun","armor","armour","spot","kill","damage","sebzés","medál","map","proxy","light","heavy","med","medium","td","tankdestroyer","block","felderités"]
finomitas = " ,".join(karomkodasok)
nagy_k = []
for szo in karomkodasok:
  szavacska = szo.capitalize()
  nagy_k.append(szavacska)

karomkodas_reakcio = [
  "Ne káromkodj légyszives!",
  "Kulturáltan vitassuk meg nézeteltéréseinket, feltevéseinket köszönöm!",
  "Oly nagy a magyar szókincsünk fejezd már ki magadat kifinomultabban!\nKöszönöm!",
  "Légyszives kulturális módon osszd meg véleményeidet, nézeteltéréseidet!\nKöszönöm!",
  
] 

@client.event

async def on_ready():
  print('Csatlakoztunk szerverhez{0.user}',
    '.format(client)')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  #if message.content == "tank" or message.content == "Tank" or message.content == "TANK" or message.content == "panzer" or message.content == "PANZER" or message.content == "panzer" or message.content == "tartály" or message.content == "páncélos" or message.content == "harckocsi" or message.content == "lánctalpas" or message.content == "harcjármű":

  msg = message.content
  
  if any(word in msg for word in tank):
    await message.add_reaction('\U0001F603')
    
  elif any(word.lower() in msg.lower() for word in tank):
    await message.add_reaction('\U0001F603')
  
  if message.content.startswith('$szia'):
    await message.channel.send('Szia!\nRemélem szép napod van!')
    
  if message.content.startswith('$listaz'):
    await message.channel.send(f'Káromkodás tárolo: {finomitas}')
    
  if message.content.startswith('$hunor'):
    await message.channel.send('Hunor_Magyar_77 wn8-a:\nhttps://hu.wot-life.com/eu/player/Hunor_Magyar_77-555872426/\nHunor_Magyar_77 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/555872426-Hunor_Magyar_77/')

  if message.content.startswith('$mpetix'):
    await message.channel.send('mpetix wn8-a:\nhttps://hu.wot-life.com/eu/player/mpetix/\nmpetix Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/528260821-mpetix/')

  if message.content.startswith('$link'):
    await message.channel.send('Klán weboldal link:\nhttps://loczylevi.github.io/HP_AL-weboldala/')

  if message.content.startswith('$osztag'):
    await message.channel.send('Jónapot klántársak, ma este 8 kor osztag aki tud jöjjön köszönöm, kire számithatok? (Ha megvan a minimum 5 klántárs akkor lesz kredit booster!)\n@everyone \n@HP_AL klántars')
  
  if message.content.startswith('$uwu'):
    await message.channel.send('༼ つ ◕_◕ ༽つ')
    
  if message.content.startswith('$wow'):
    await message.channel.send('╰(°▽°)╯')
    
  if message.content.startswith('$noice'):
    await message.channel.send('(❁´◡`❁)')
    
  if message.content.startswith('$smile'):
    await message.channel.send('(●´◡`●)')
    
  if message.content.startswith('$nemtom'):
    await message.channel.send('¯\_(ツ)_/¯')
  
  if message.content.startswith('$pasz'):
    await message.channel.send('¯\_(ツ)_/¯')
    
  if message.content.startswith('$hmm'):
    await message.channel.send('( ͡° ͜ʖ ͡°)')
    
  if message.content.startswith('$hm'):
    await message.channel.send('( ͡° ͜ʖ ͡°)')
    
  if message.content.startswith('$boosterban'):
    await message.channel.send('Boosterban táblázat link:\n https://docs.google.com/spreadsheets/d/16R8YCex7kfdwkaBeoY_Mnl3l8g2wGnp0D3EPeFVQ2Ws/edit#gid=1409607917')
    
  if message.content.startswith('$segitseg'):
    await message.channel.send('Discord HP_AL szerver bot parancsok:\nmindent $-dollár jellel kell kezdeni\n$jatékosnév --> játékos wm8, wot stat (csak klántársaknál működik)\n$link --> Klán weboldal link\n$uwu --> ༼ つ ◕_◕ ༽つ\n$boosterban --> Megtekinthető a boosterban táblázat (a táblázat mellet jobbra levan írva miről van szó aki nem tudja)\n$osztag --> osztag felhivás\n$szabalyzat --> DC Szabályok\n$wow --> ╰(°▽°)╯\n$noice --> (❁´◡`❁)\n$smile --> (●´◡`●)\n$pasz vagy nemtom --> ¯\_(ツ)_/¯\n$hm --> ( ͡° ͜ʖ ͡°)\n<<< Jogosultság szükséges ezeknél a parancsoknál >>>\n$kirug @felhasználónév --> kirugja a felhasználót\n$kitilt @felhasználónév --> kirugja a felhasználót véglegesen\n(Ha bármi hibát észleltél, vagy ötleteid vannak fejlesztésben akkor nyugodtan írj rám köszi!) bot készitő: @loczypista2003#3097')
    
  if message.content.startswith('$help'):
   await message.channel.send('Discord HP_AL szerver bot parancsok:\nmindent $-dollár jellel kell kezdeni\n$jatékosnév --> játékos wm8, wot stat (csak klántársaknál működik)\n$link --> Klán weboldal link\n$uwu --> ༼ つ ◕_◕ ༽つ\n$boosterban --> Megtekinthető a boosterban táblázat (a táblázat mellet jobbra levan írva miről van szó aki nem tudja)\n$osztag --> osztag felhivás\n$szabalyzat --> DC Szabályok\n$wow --> ╰(°▽°)╯\n$noice --> (❁´◡`❁)\n$smile --> (●´◡`●)\n$pasz vagy nemtom --> ¯\_(ツ)_/¯\n$hm --> ( ͡° ͜ʖ ͡°)\n<<< Jogosultság szükséges ezeknél a parancsoknál >>>\n$kirug @felhasználónév --> kirugja a felhasználót\n$kitilt @felhasználónév --> kirugja a felhasználót véglegesen\n(Ha bármi hibát észleltél, vagy ötleteid vannak fejlesztésben akkor nyugodtan írj rám köszi!) bot készitő: @loczypista2003#3097')
    
  if message.content.startswith('$szabalyzat'):
    await message.channel.send('1.Nincs káromkodás!\nMagától értetődik kulturális módon osszuk meg véleményeinket és nézet eltéréseinket! (A bot ki töröl bármi fajta káromkodást)\n2.Veszélyes linkek/weboldalak megosztása tilos!\nSenki sem szereti ha virus van a gépén\n3.Print screen gomb használata\nEgy kép minősége legyen fontos...Ez olyan mintha egy ünnepségre szakadt polót vennénk.... Kérlek szépen ha képernyő fotot készítesz használd a (laptopnál "PrtSc" gombot) Print Screen gombot köszi :)\n4.Klán és wottal kapcsolatos témák\nNem azért jön fel ide az ember hogy lássa milyen olcsó a kenyér "x" Áruházba...Arra megvannak a más csoportok/reklámok\n5. 2 hét próbaidő\nEgy újonc a klánból nem lèphet be egyből a Facebook csoportba csak akkor ha letelt a 14 nap próba idő!!!\n6.Nincs politizálás!\n7.Nincs semmi fajta elitélés!\nNe csesztessük egymást, veszekedjünk.. Stb...')

  if message.content.startswith('$marcibercike'):
    await message.channel.send('marcibercike wn8-a:\nhttps://hu.wot-life.com/eu/player/marcibercike/\nmarcibercike Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/536753037-marcibercike/')
    
  if message.content.startswith('$Tankbit3_HUN'):
    await message.channel.send('Tankbit3_HUN wn8-a:\nhttps://hu.wot-life.com/eu/player/Tankbit3_HUN-573571663/\nTankbit3_HUN Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/573571663-Tankbit3_HUN/')

  if message.content.startswith('$Ali3n_x3'):
    await message.channel.send('Ali3n_x3 wn8-a:\nhttps://hu.wot-life.com/eu/player/ALi3n_x3-507844152/\nAli3n_x3 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/507844152-ALi3n_x3/')

  if message.content.startswith('$dominiknunkovics'):
    await message.channel.send('dominiknunkovics wn8-a:\nhttps://hu.wot-life.com/eu/player/dominiknunkovics-525707300/\ndominiknunkovics Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/525707300-dominiknunkovics/')

  if message.content.startswith('$325_stern'):
    await message.channel.send('325_stern wn8-a:\nhttps://hu.wot-life.com/eu/player/325_stern-516977718/\n325_stern Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/516977718-325_stern/')

  if message.content.startswith('$medve111'):
    await message.channel.send('medve111 wn8-a:\nhttps://hu.wot-life.com/eu/player/medve111/\nmedve111 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/555106644-medve111/')

  if message.content.startswith('$FreeeHUN'):
    await message.channel.send('FreeeHUN wn8-a:\nhttps://hu.wot-life.com/eu/player/FreeeHUN-507169661/\nFreeeHUN Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/507169661-FreeeHUN/')

  if message.content.startswith('$kapitany173'):
    await message.channel.send('kapitany173 wn8-a:\nhttps://hu.wot-life.com/eu/player/kapitany173-533722694/\nkapitany173 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/533722694-kapitany173/')

  if message.content.startswith('$mytezoo'):
    await message.channel.send('mytezoo wn8-a:\nhttps://hu.wot-life.com/eu/player/mytezoo-564435329/\nmytezoo Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/564435329-mytezoo/')

  if message.content.startswith('$tjoe67'):
    await message.channel.send('tjoe67 wn8-a:\nhttps://hu.wot-life.com/eu/player/tjoe67/\ntjoe67 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/505979795-tjoe67/')

  if message.content.startswith('$Unstoppabe'):
    await message.channel.send('Unstoppabe wn8-a:\nhttps://hu.wot-life.com/eu/player/Unstoppabe/\nUnstoppabe Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/554821859-Unstoppabe/')

  if message.content.startswith('$RubenRambo'):
    await message.channel.send('RubenRambo wn8-a:\nhttps://hu.wot-life.com/eu/player/RubenRambo-545153732/\nRubenRambo Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/545153732-RubenRambo/')

  if message.content.startswith('$zsolti_12_2015'):
    await message.channel.send('zsolti_12_2015 wn8-a:\nhttps://hu.wot-life.com/eu/player/zsolti_12_2015-529349173/\nzsolti_12_2015 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/529349173-zsolti_12_2015/')

  if message.content.startswith('$Ati_pikus'):
    await message.channel.send('Ati_pikus wn8-a:\nhttps://hu.wot-life.com/eu/player/Ati_pikus-582388259/\nAti_pikus Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/582388259-Ati_pikus/')

  if message.content.startswith('$Atesz1230'):
    await message.channel.send('Atesz1230 wn8-a:\nhttps://hu.wot-life.com/eu/player/Atesz1230-549778498/\nAtesz1230 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/549778498-Atesz1230/')

  if message.content.startswith('$Tutifruti0323'):
    await message.channel.send('Tutifruti0323 wn8-a:\nhttps://hu.wot-life.com/eu/player/Tutifruti0323-547454643/\nTutifruti0323 Wot statja:\nhttps://worldoftanks.eu/en/community/accounts/547454643-Tutifruti0323/')
    
  if message.content.startswith('$szopnifogsz'):
    await message.channel.send('szopnifogsz wn8-a:\nhttps://wot-life.com/eu/player/szopnifogsz-582784349/\nWot statja:\nhttps://worldoftanks.eu/en/community/accounts/582784349-szopnifogsz/')
      
  #karomkodas kereso
  if any(word in msg for word in karomkodasok):
    await message.channel.send(random.choice(karomkodas_reakcio))
    await message.channel.send('Töröltük az üzenetet! Káromkodás miatt.')
    await message.delete()
    
  #nagybetüs karomkodasok
  elif any(word in msg for word in nagy_k):
    await message.channel.send(random.choice(karomkodas_reakcio))
    await message.channel.send('Töröltük az üzenetet! Káromkodás miatt.')
    await message.delete()

  elif any(word.lower() in msg.lower() for word in karomkodasok):
    await message.channel.send(random.choice(karomkodas_reakcio))
    await message.channel.send('Töröltük az üzenetet! Káromkodás miatt.')
    await message.delete()
    
@client.event
async def on_reaction_add(reaction, user):
  await reaction.message.channel.send(f"{user} felhasználó reagált ezzel: {reaction.emoji}")

#keep_alive()
client.run(os.environ["DISCORD_TOKEN"])
#uwu
# ez eddig is marha nagy! ________________________