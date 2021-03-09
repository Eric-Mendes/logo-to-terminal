# logo-to-terminal
|<img src="https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg" width=25>|[Read this in English](https://github.com/Eric-Mendes/logo-to-terminal/blob/main/README.en.md "README.md in English")|
|---|:--|


Com isto você pode mostrar qualquer icon em preto e branco como texto no terminal.

## Motivação
Back-end não precisa ser *visualmente* desinteressante. Pensando nisso e inpirado [neste problema](https://www.hackerrank.com/challenges/text-alignment/problem "Ver o problema") do Hackerrank que criei este código.

## Como funciona
Usando a biblioteca [PIL](https://pillow.readthedocs.io/en/stable/ "Ler os docs") para lidar com as imagens e [numpy](https://numpy.org/ "Ir para o site do numpy") para transformar imagens em um array 2D de inteiros, este código mapeia a cor preta de uma imagem (255) para o símbolo \#, e a cor branca (0) para um espaço em branco.

## Exemplo de uso
A imagem abaixo:

<img src="https://logoeps.com/wp-content/uploads/2014/09/49068-linkedin-logo-icon-vector-icon-vector-eps.png" alt="linkedin logo" />

Vira:

```
                 
 ###             
 ###             
 ###             
                 
                 
 ###  ### #####  
 ###  ########## 
 ###  ##### #### 
 ###  ####   ### 
 ###  ###    ### 
 ###  ###    ### 
 ###  ###    ### 
 ###  ###    ### 
 ###  ###    ### 
 ###  ###    ### 
                 


```

<hr/>

Este resultado pode ser obtido da seguinte maneira
```
from Icon import Icon

if __name__ == '__main__':
    ic = Icon('/home/user/desktop/linkedin-logo.png', 15)
    print(ic)

```

## Para usar
**Deixe uma star**, baixe o arquivo que contém a classe Icon, pip instale as dependências e use como você usaria qualquer outra classe.
