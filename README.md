# Divisão de Conjuntos de Dados de Imagens com split-folders

Este script Python utiliza a biblioteca split-folders para dividir um conjunto de dados de imagens em conjuntos de treinamento, validação e teste com proporções especificadas ou um número fixo de itens por conjunto.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. Você pode instalar a biblioteca split-folders usando pip:

```pip install split-folders```


## Utilização

1. Clone este repositório ou copie o script para o seu projeto.
2. Certifique-se de ter uma pasta contendo suas imagens de entrada. O nome da pasta é especificado na variável input_folder.
3. Execute o script Python.

## Estrutura do Projeto

images_input/: Pasta contendo as imagens de entrada.
images_output/: Pasta de saída onde os conjuntos de dados divididos serão salvos.

## Executando o Script

```python split_images.py```

## Detalhes do Script

1. Este script divide o conjunto de dados de entrada em conjuntos de treinamento, validação e teste com proporções especificadas.
2. Você pode ajustar as proporções de treinamento, validação e teste ajustando as variáveis Train, validation e test no script.
3. Você também pode ajustar o número fixo de itens por conjunto alterando os valores passados para fixed na função splitfolders.fixed().
4. Certifique-se de que a estrutura da sua pasta de entrada esteja correta, com subpastas contendo imagens correspondentes a cada classe.

Para mais informações sobre o split-folders, consulte a documentação oficial: split-folders no [GitHub](https://github.com/jfilter/split-folders)




