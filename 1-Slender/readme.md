# Slender

Vírus do episódio 1 de KVR

- Alvo: Scripts de python no mesmo diretório que ele;
- Linguagem: Python;
- Mecanismo de busca: Todos os arquivos python que se encontram no mesmo diretório que ele;
- Mecanismo de reprodução: Se não identificar assinatura no começo do arquivo alvo, copia todas as primeiras 25 linhas no início do arquivo alvo;
- Bomba lógica: Nenhuma

## Precauções:

- Executar em um diretório controlado com outros scripts python que já se sabe que se quer testar;

## Identificando:

- Assinatura # 123456 no início de arquivos infectados;

## Profilaxia:

- Remover as primeiras 25 linhas de todos os arquivos infectados;
    Não executar arquivos infectados.
