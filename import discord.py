import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$bilgi 1'):
        await message.channel.send("Londra, dünyanın merkezidirLondra’nın güneydoğusunda yer alan bir kasaba olan Greenwich, Kraliyet Gözlemevi'ni bulacağınız yerdir. 0° boylamı olarak adlandırılan ve dünyanın başlangıç meridyeninin bulunduğu yer olan Greenwich, aynı zamanda Birleşik Krallık'ın en büyük ikinci gözlemevidir.")
    elif message.content.startswith('$bilgi 2'):
        await message.channel.send("Dünya atmosferi yaklaşık 10 bin kilometre uzunluğundadır:Evrenin sonsuzluk kavramı insan aklının alabileceğinden çok daha karmaşık bir mesele olabileceği için bazı mesafe kavramları bize epey şaşırtıcı gelebilir. Ancak koskoca evreni düşündüğümüz zaman gezegenimizin atmosferinin 10 bin kilometre olması küçücük bir detaydır.")

    elif message.content.startswith('$bilgi  3'):
            await message.channel.send("Hapşırdığınızda beyin hücrelerinizin bir kısmının öldüğünü biliyor muydunuz? Ya da hayatınızın yaklaşık 6'da 1'inin çarşamba günlerinde geçtiğini duymuş muydunuz? Birazdan okuyacağınız ilginç bilgiler size tüm bildiklerinizi unutturacak.")

    
    elif message.content.startswith('$bilgi 4'):
            await message.channel.send("Futbol oyuncularının çoğu, bir maç sırasında ortalama 11 km koşar.")
    elif message.content.startswith('$bilgi 5'):
            await message.channel.send("Yalnızca tavşanlar ve papağanlar, kafalarını çevirmeden arkalarını görebilirler.")
    elif message.content.startswith('$bilgi 6'):
            await message.channel.send("Kırbacın çatlama sesi çıkarmasının sebebi, ucunun sesten daha hızlı hareket etmesidir.")
    elif message.content.startswith('$bilgi 7'):
            await message.channel.send("itanik'in inşasına 7 milyon dolar harcanmıştı. Filmin maliyeti ise 200 milyon dolardı.")
    elif message.content.startswith('$bilgi 8'):
            await message.channel.send("Su aygırları üzüldüklerinde terleri kırmızı renk alır.")
    elif message.content.startswith('$bilgi 9'):
            await message.channel.send("Kalbin yeri dolayısıyla sol akciğer, sağdakinden daha küçüktür.")
    elif message.content.startswith('$bilgi 9'):
            await message.channel.send("Gülmek, stres hormonunu azaltır ve bağışıklık sistemini güçlendirir. 6 yaşındaki bir çocuk günde ortalama 300 kez gülerken, yetişkinler yalnızca 15-100 kez gülerler.")
    elif message.content.startswith('$bilgi 10'):
            await message.channel.send("Soğan doğrarken sakız çiğnerseniz ağlamazsınız.")
    elif message.content.startswith('$bilgi 11'):
            await message.channel.send("Dönmeye çalışırken kanatları kopmayacak olsa, Boeing 747 ters bir şekilde uçabilecek sisteme sahiptir.")
    elif message.content.startswith('$bilgi 12'):
            await message.channel.send(" İpek böcekleri, 56 günde kendi ağırlıklarının 86.000 katı kadar beslenirler.")
    elif message.content.startswith('$bilgi 13'):
            await message.channel.send("hapşırırken burnunuzu ve ağzınızı aynı anda asla kapamayın; gözleriniz yerinden çıkabilir.")
    elif message.content.startswith('$bilgi 14'):
            await message.channel.send("Madison'daki bir matematik öğretmeninin sahip olduğu dünyanın en zeki domuzu çarpım tablosunu 12'lere kadar ezberlemişti.")
    elif message.content.startswith('$bilgi 15'):
            await message.channel.send("Antik Yunan'da zengin aile çocukları hayatları boyunca kılsız olmaları için doğdukları anda zeytinyağına batırılırlardı.")
    elif message.content.startswith('$bilgi 16'):
            await message.channel.send("Her Labrador retriever, ara sıra muzlar hakkında rüya görür.")
    elif message.content.startswith('$bilgi 17'):
            await message.channel.send("Hayatınızın yaklaşık 6'da 1'i çarşamba günlerinde geçer.")
    elif message.content.startswith('$bilgi 18'):
            await message.channel.send("Ucunu açacağınız kalemi alüminyum folyoya sararak kalemtıraşınızın bıçaklarını keskinleştirebilirsiniz")
    elif message.content.startswith('$bilgi 19'):
            await message.channel.send(" 7. 111.111.111 x 111.111.111 = 12.345.678.987.654.321")
    elif message.content.startswith('$bilgi 20'):
            await message.channel.send("Her gün 12 yeni doğan bebek yanlış aileye veriliyor.")
    elif message.content.startswith('$bilgi 21'):
            await message.channel.send("Amerikan otoyollarında yaklaşık 123.000.000 araba kullanılıyor.")
    elif message.content.startswith('$bilgi 22'):
            await message.channel.send(" Dünyanın en geniş yolu olan Brezilya'daki Anıtsal Eksen'de 160 araba yan yana gidebilir.")
    elif message.content.startswith('$bilgi 23'):
            await message.channel.send("Hamam böcekleri kafaları kopsa bile birkaç hafta daha yaşayabilirler.")
    elif message.content.startswith('$bilgi 24'):
            await message.channel.send(" Tayvanlı bir şirket, buğdaydan, yenebilen mutfak gereçleri üretiyor.")
    elif message.content.startswith('$kodland platform'):
            await message.channel.send(" İnekler, bir günde insanlardan 200 kat daha fazla gaz üretirler.")
    elif message.content.startswith('$bilgi 25'):
            await message.channel.send("On sentlik paraların kenarları boyunca 118 kabartma çizgisi bulunur.")
    elif message.content.startswith('$bilgi 26'):
            await message.channel.send(" Yusufçukların ömürleri yaklaşık 24 saattir.")
    elif message.content.startswith('$bilgi 27'):
            await message.channel.send(" Zürafalar yaklaşık 53 cm'lik dilleri ile kendi kulaklarını temizleyebilirler.")
    elif message.content.startswith('$bilgi 28'):
           await message.channel.send(" Zürafalar susuzluğa devlerden daha iyi dayanırlar")
    elif message.content.startswith('$bilgi 29'):
            await message.channel.send("Gıda renklendiricileri eklenmeseydi eğer, kolanın rengi yeşil olurdu.")
    elif message.content.startswith('$bilgi 30'):
            await message.channel.send("Suudi Arabistan'da kadın kocasına kahve yapmazsa boşanma yaşanabilir-Tebrikler ilk ayı başaru ile tamamladınız")
   
client.run("token")