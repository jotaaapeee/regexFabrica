import re

#O site que deve utilizar é o https://g1.globo.com/ para a realização do seu exercício.

#Nos sites de notícias, é comum encontrarmos páginas com uma lista de links para as notícias publicadas, como por exemplo, a seção sobre política ou sobre esportes. Chamamos essas páginas de **editorias**.

#EXERCICIO
#Seu segundo exercício será composto por duas partes.

#Na primeira, mais simples, você deve identificar o padrão de urls de editorias e notícias de um determinado site e escrever um (ou mais) regex para cada tipo que encontrar. **Obs.: no mínimo um para cada tipo.**

txt_edit = """https://g1.globo.com/sp
https://g1.globo.com/ba
https://g1.globo.com/rj
https://g1.globo.com/sp
https://g1.globo.com/politica
"""
#Regex para capturar Editorias
regex_edit = re.compile(r'g1.globo.com/[\w-]+/')
#usar no restritivo --> /index/


txt_noti = """https://g1.globo.com/sp/santos-regiao/noticia/2023/01/31/homem-e-preso-por-espancar-e-estuprar-a-ex-esposa-mensagens-revelam-ameacas-de-morte-e-requintes-de-crueldade.ghtml
https://g1.globo.com/ba/bahia/noticia/2023/01/31/professor-de-futebol-denunciado-por-estupro-de-adolescente-na-bahia-e-arbitro-esportivo-ha-mais-de-15-anos.ghtml
https://g1.globo.com/rj/rio-de-janeiro/noticia/2023/01/31/policia-faz-operacao-em-comunidade-da-zona-oeste-do-rio-para-tentar-encontrar-presos-que-fugiram-de-presidio-em-bangu.ghtml
https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2023/01/31/policia-federal-flagra-quase-300-kg-de-cocaina-escondidos-no-casco-de-navio-no-porto-de-sao-sebastiao.ghtml
https://g1.globo.com/politica/blog/andreia-sadi/post/2023/01/31/na-vespera-de-atos-terroristas-pf-recomendou-que-transito-de-caravanas-de-bolsonaristas-na-esplanada-dos-ministerios-fosse-impedido.ghtml"""
#Regex para capturar Noticias
regex_noti = re.compile(r'g1.globo.com/([\w-]+|[\w-]+/[\w-]+|[\w-]+/[\w-]+/[\w-]+|[\w-]+/[\w-]+/[\w-]+/[\w-]+)/(noticia|blog)')


#Na segunda parte, você deve escrever regex para encontrar o título, a data de publicação e o texto das notícias desse mesmo site.

txt_titulo = """<h1 class="content-head__title" itemprop="headline">Governo Bolsonaro promoveu 'desmanche' no combate à corrupção, diz Transparência</h1>"""

regex_titulo = re.compile(r'"""<h1 class="content-head__title" itemprop="headline">(.*?)</h1>(.*)"""gmis')

txt_data = """<time itemprop="datePublished" datetime="2023-01-31T05:01:16.783Z"> 31/01/2023 02h01 <div></div></time>"""

regex_data = re.compile(r'<time itemprop="datePublished" datetime="(.*?)T(.*)')


txt_texto = """<article itemprop="articleBody"> A avaliação faz parte do relatório global que mede a percepção sobre a corrupção em 180 países. O Brasil ficou em 94ª lugar no ranking mundial, considerado um desempenho ruim pela organização. <div class="block-podcast">"""

regex_texto = re.compile(r'<article itemprop="articleBody">(.*?)<div class="block-podcast">')