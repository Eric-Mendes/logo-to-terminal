# logo-to-terminal
Com isto você pode mostrar qualquer icon em preto e branco como texto no terminal.

## Motivação
Back-end não precisa ser *visualmente* desinteressante. Foi pensando nisso que criei este código.<br/>
Usando a biblioteca [PIL](https://pillow.readthedocs.io/en/stable/ "Ler os docs") para lidar com as imagens e [numpy](https://numpy.org/ "Ir para o site do numpy") para transformar imagens em um array 2D de inteiros, este código mapeia a cor preta de uma imagem (255) para o símbolo \#, e a cor branca (0) para um espaço em branco.

## Para rodar
Após instalar todos imports necessários, basta abrir o terminal e rodar como qualquer outro script, por exemplo:
```
python3 main.py
```

## Futuramente...
Pretendo transformar isto em uma lib para todos usarem em seus projetos.
