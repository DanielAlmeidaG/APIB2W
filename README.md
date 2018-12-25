# APIB2W
API Rest desenvolvida com python e sqlite

Acabei desenvolvendo com sqlite pois é o banco que tenho mais familiaridade, pelo fato de usar no meu emprego atual.

Para utulizar a API, basta executar o arquivo "run.py" e acessar o endereço http://127.0.0.1:5000/planet/{nome ou id do planeta desejado}

Para inserir e deletar um planeta utilizei o programa "Postman" para testar.
  Para deletar, é necessario apenas definir o modo Delete e na url inserir http://127.0.0.1:5000/planet/{nome ou id do planeta desejado}
  Para inserir, é necessaria apenas definir o modo Post, na url inserir http://127.0.0.1:5000/planet/{nome do planeta} e passar um json com:
    -Nome
    -Clima
    -Terreno
    -Aparições
    
A busca na API do Star Wars disponibilizada é feita automaticamente quando o arquivo "run.py" é executado.
