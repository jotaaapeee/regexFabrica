import re

#O site que deve utilizar é o https://tecnoblog.net/ para a realização do seu exercício.

#Nos sites de notícias, é comum encontrarmos páginas com uma lista de links para as notícias publicadas, como por exemplo, a seção sobre política ou sobre esportes. Chamamos essas páginas de **editorias**.
#Seu segundo exercício será composto por duas partes.

#EXERCICIO

#Na primeira, mais simples, você deve identificar o padrão de urls de editorias e notícias de um determinado site e escrever um (ou mais) regex para cada tipo que encontrar. **Obs.: no mínimo um para cada tipo.**

txt_noti = """
https://tecnoblog.net/noticias/2023/01/30/oi-fibra-aumenta-preco-de-internet-banda-larga-em-99-cidades/
https://tecnoblog.net/achados/2023/01/30/tv-qled-de-55-da-samsung-chega-a-um-dos-melhores-precos-historicos-em-oferta/
https://tecnoblog.net/noticias/2023/01/30/twitter-prepara-o-terreno-para-se-tornar-uma-plataforma-de-pagamentos/
https://tecnoblog.net/achados/2023/01/24/iphone-13-ganha-ate-r-3-500-de-desconto-em-oferta-com-cashback/
https://tecnoblog.net/noticias/2023/01/30/microsoft-e-openai-rebatem-acao-que-acusa-ia-do-github-de-violar-copyright/
"""

#Regex para Noticia
regex_noti_acha = re.compile(r'tecnoblog.net/(noticias|achados)/\d{4}\/\d{2}\/\d{2}\/[\w-]+\/')

#Regex para achar outros links de noticia
regex_outros = re.compile(r'tecnoblog.net/[\w-]+/\w+-\w+-\w+-[\w-]+/$')
#Colocar no Restritivo --> /stories/


txt_edit = """
https://tecnoblog.net/tema/software-apps/
https://tecnoblog.net/tema/games-jogos/
https://tecnoblog.net/tema/negocios/
https://tecnoblog.net/tema/nacional/
https://tecnoblog.net/tema/computador-e-pc/
https://tecnoblog.net/tema/seguranca/
https://tecnoblog.net/tema/financas/
https://tecnoblog.net/tema/cultura-2/
https://tecnoblog.net/tema/ciencia/
https://tecnoblog.net/tema/carros/
https://tecnoblog.net/tema/curiosidades/
https://tecnoblog.net/tema/tecnoblog/
"""
#Regex para editorias
regex_editorias = re.compile(r'tecnoblog.net/[\w-]+/$')
#Colocar no Restritivo --> /anuncie/|/vagas/|/sobre/$|/contato/|/etica/|/politica-de-privacidade/

#Regex para editorias especificas
regex_edi_espcf = re.compile(r'tecnoblog.net/(tema|sobre)/[\w-]+/$')


#Na segunda parte, você deve escrever regex para encontrar o título, a data de publicação e o texto das notícias desse mesmo site.

txt_titulo = """<h1 class="flipboard-title title" itemprop="headline">Sony comemora fim da escassez do PS5 com vídeo inédito</h1>"""

#Regex que captura o titulo
regex_titulo = re.compile(r'<h1 class=flipboard-title title itemprop=headline>(.*?)</h1>(.*)')


txt_data = """<time datetime="2023-01-30T19:10:43+00:00">30/01/2023 às 16:10</time>"""

#Regex que captura a data
regex_data = re.compile(r'<time datetime=(.*?)T(.*)')


txt_texto = """<div class="entry grid8">
<p>Após o lançamento do PlayStation 5 em 12 de novembro de 2020, os fãs da plataforma se depararam com uma grande escassez do console devido à falta de chips no planeta. Contudo, pouco mais de dois anos depois, a Sony anunciou que esse problema parece ter chegado ao fim. Em uma postagem no blog da marca, a japonesa afirmou que “agora você deve ter muito mais facilidade em encontrar um PS5 em varejistas em todo o mundo”.</p>
<nav class="tags">
<a href="https://tecnoblog.net/sobre/chip/" rel="tag">chip</a><a href="https://tecnoblog.net/sobre/playstation-5/" rel="tag">PlayStation 5</a><a href="https://tecnoblog.net/sobre/ps-vr2/" rel="tag">PS VR2</a><a href="https://tecnoblog.net/sobre/sony/" rel="tag">Sony</a> </nav>
</div>"""

#Regex que captura o texto
regex_texto = re.compile(r'<div class=entry grid8>(.*?)<nav class=tags>')

