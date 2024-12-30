## **Descrição:**

Nesse exercício do Cs50 é feito um programa que valida se uma sequência de DNA específica pode ser encontrada em um banco de dados que está em formato csv e caso seja retorna á quem pertence.

Com ele o foco é em receber argumentos do sistema, trabalhar com arquivos csv, listas e dicionários também, espero que gostem da minha solução para esse problema. 👍🤖


### **1. Sistema Operacional:**
O projeto foi desenvolvido para ser executado em **Windows** (testado com **Windows 11**).



## **2. Tecnologias Utilizadas:**

- **Backend:** Linguagem **Python**, com uso das bibliotecas **os**, **sys**, **re** e **csv**.

## **Fluxo de Instalação e Execução:**

### **Passo 1: Baixar o Projeto.**
```bash

#### Via Git:
Clone o repositório para seu diretório local.

git clone https://github.com/cauanmorais/dna_project_cs50.git

Via ZIP: Baixe o arquivo ZIP do repositório e extraia-o em um diretório de sua escolha.

## Testar o Sistema

Com a configuração correta você pode usar o programa para validar correspondências em uma vasta gama de arquivos, mas de primeira te incentivo a testar da seguinte maneira.

Rode seu programa como python dna.py  \databases\large.csv  \sequences\1.txt
o Programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\small.csv  \sequences\1.txt
O programa deve retornar:
DNA corresponde a: Bob

Rode seu programa como  > python dna.py  \databases\small.csv  \sequences\2.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\small.csv  \sequences\3.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\small.csv  \sequences\4.txt
O programa deve retornar:
DNA corresponde a: Alice.

Rode seu programa como  > python dna.py  \databases\small.csv  \sequences\5.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\5.txt
O programa deve retornar:
DNA corresponde a: Lavender.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\6.txt
O programa deve retornar:
DNA corresponde a: Luna.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\7.txt
O programa deve retornar:
DNA corresponde a: Ron.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\8.txt
O programa deve retornar:
DNA corresponde a: Ginny.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\9.txt
O programa deve retornar:
DNA corresponde a: Draco.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\10.txt
O programa deve retornar:
DNA corresponde a: Albus.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\11.txt
O programa deve retornar:
DNA corresponde a: Hermione.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\12.txt
O programa deve retornar:
DNA corresponde a: Lily.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\13.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\14.txt
O programa deve retornar:
DNA corresponde a: Severus.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\15.txt
O programa deve retornar:
DNA corresponde a: Sirius.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\16.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\17.txt
O programa deve retornar:
DNA corresponde a: Harry.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\18.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\19.txt
O programa deve retornar:
DNA corresponde a: Fred.

Rode seu programa como  > python dna.py  \databases\large.csv  \sequences\20.txt
O programa deve retornar:
Nenhuma correspondência encontrada.

### Observações Importantes
1. Certifique-se de usar o caminho correto para onde você armazenou os arquivos de csv.
2. O programa deve ser iniciado com dois argumentos + "python", no windows seria algo como python dna.py (caminho para o banco de dados) + (arquivo para procurar no banco).

---
```

## Contribuições:

Se você deseja contribuir para o projeto, clone o repositório e faça suas alterações. Em seguida, envie um pull request com suas melhorias.

## Licença:

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.