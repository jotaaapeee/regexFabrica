import re

#O site que deve utilizar é o https://www.r7.com/ para a realização do seu exercício.

#Nos sites de notícias, é comum encontrarmos páginas com uma lista de links para as notícias publicadas, como por exemplo, a seção sobre política ou sobre esportes. Chamamos essas páginas de **editorias**.

#Exercicio 
#Seu segundo exercício será composto por duas partes.

#Na primeira, mais simples, você deve identificar o padrão de urls de editorias e notícias de um determinado site e escrever um (ou mais) regex para cada tipo que encontrar. **Obs.: no mínimo um para cada tipo.**

#Regex para capturar Noticias
text_noti = """https://a10mais.com/noticias/policia/ufpi-abre-sindicancia-para-definir-punicao-de-mestrando-suspeito-de-estuprar-e-matar-janaina-bezerra-9941.html
http://noticias.r7.com/cidades/veja-o-que-se-sabe-sobre-a-investigacao-do-estupro-e-feminicidio-de-estudante-no-piaui-31012023
http://noticias.r7.com/saude/mulher-desenvolve-cancer-de-pele-apos-ter-o-dedo-cortado-por-manicure-31012023
http://noticias.r7.com/saude/mulher-desenvolve-cancer-de-pele-apos-ter-o-dedo-cortado-por-manicure-31012023
"""

regex_noti = re.compile(r'[\w+]*\.[\w+\/-\/.-]+')

#Regex para capturar Editorias
text_edi = """https://esportes.r7.com/brasilia
https://noticias.r7.com/carros
https://noticias.r7.com/economia
https://noticias.r7.com/minas-gerais
https://esportes.r7.com/futebol
"""

regex_edi = re.compile(r'[\w+]*\.[\w+\/-\/.-]+\/')

#Na segunda parte, você deve escrever regex para encontrar o título, a data de publicação e o texto das notícias desse mesmo site.

txt_titulo = """<h1 class="toolkit-title">
     MP-SP analisa pedido de prisão de aluna da USP por desvio de dinheiro de formatura
    </h1>
"""

regex_titulo = re.compile(r'<h1 class="toolkit-title">(.*?)</h1>(.*)')


txt_data = """<time datetime="2023-01-31T11:01:00-03:00" class="toolkit-signature__publication-time">
          31/01/2023 - 11h01
            <span class="toolkit-signature__publication-update">
              (Atualizado em 31/01/2023 - 11h30)
            </span>
        </time>
"""

regex_data = re.compile(r'<time datetime="(.*?)T(.*)')


txt_texto = """<article class="toolkit-media-content"><p>
	O MP-SP (Ministério Público de São Paulo) informou que vai analisar as informações colhidas pela polícia e o <a href="https://noticias.r7.com/sao-paulo/policia-conclui-inquerito-e-pede-prisao-de-aluna-da-usp-por-desvio-de-dinheiro-de-formatura-30012023" target="_blank"><strong>pedido de prisão de Alicia Dudy Müller</strong></a>, aluna de medicina da USP (Universidade de São Paulo) acusada de desviar o dinheiro da formatura da turma.</p>
<p>
	A análise do órgão pode levar ao oferecimento de denúncia contra a estudante perante a Justiça ou a requisição de investigações complementares ao delegado responsável.</p><ul class="toolkit-tags__list">
"""

regex_titulo = re.compile(r'<article class="toolkit-media-content">(.*?)<ul class="toolkit-tags__list">')