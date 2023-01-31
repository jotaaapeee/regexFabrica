import re

#EXERCICIO 1
#Faça um regex para capturar os cpfs presentes no trecho abaixo. Obs.: o regex precisa casar com cpfs com ou sem pontuação (772.843.809-34 ou 77284380934)
txt_1 = """Maria foi ao Na Hora e recebeu seu novo CPF (772.843.809-34), porém, para confirmar o número do seu novo documento, foi pedido que na hora de digitar no sistema, que digitasse sem a pontuação, então ela digitou 77284380934."""

regex_1 = (r'(\d{3}\.\d{3}\.\d{3}\-\d{2})|(\d{11})')

match_1 = re.match(regex_1, txt_1)

print(match_1)


#EXERCICIO 2
#Encontre a data e hora no texto abaixo.
txt_2 = """O sistema vai parar para uma manutenção programada no dia 10/09/2020 às 23:00."""

regex_2 = re.compile(r'(\d{2}\/\d{2}\/\d{4})|(\d\d:[0-5]\d)')

match_2 = re.match(regex_2, txt_2)

print(match_2)


#EXERCICIO 3
#Escreva um regex que encontre o conteúdo do atributo href do link no html a seguir (somente o endereço).
txt_3 = """html
<html>
  <head><title>Exercícios</title></head>
  <body>
    <p>Menu</p>
    <ul>
      <li><a href="https://google.com">Google</a></li>
    </ul>
</html>"""

regex_3 = re.compile(r'href=\"((http?s:\/\/)(\w{2,}\.\w{2,}))')

match_3 = re.match(regex_3, txt_3)

print(match_3)


#EXERCICIO 4
#Encontre o texto dentro da tag h1 abaixo.
txt_4 = """html
<html>
  <head><title>Exercícios</title></head>
  <body>
    <h1>Exercícios</h1>
    <table>
      <thead>
        <th>#</th>
        <th>Questão</th>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Primeiro exercício de regex</td>
        </tr>
      </tbody>
    </table>
</html>"""

regex_4 = re.compile(r"<h1>(\w{2,})")

match_4 = re.match(regex_4, txt_4)

print(match_4)
