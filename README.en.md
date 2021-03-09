# logo-to-terminal
|<img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1200px-Flag_of_Brazil.svg.png" width=25>|[Ler isto em português](https://github.com/Eric-Mendes/logo-to-terminal "README.md em português")|
|---|:--|

Show a black and white Icon as text on terminal.

## Motivation
Back-end doesn't have to be *visually* "uniteresting". With that in mind (and also inpired by [this](https://www.hackerrank.com/challenges/text-alignment/problem "See the problem") Hackerrank problem) I created this code.

## How it works
Using [PIL](https://pillow.readthedocs.io/en/stable/ "Read the docs") to deal with the images and [numpy](https://numpy.org/ "Go to numpy's website") to turn them into a 2D array of integers, this code maps the color black (255) to the symbol \# and the color white (0) to a whitespace.

## Usage example
This image

<img src="https://logoeps.com/wp-content/uploads/2014/09/49068-linkedin-logo-icon-vector-icon-vector-eps.png" alt="linkedin logo" />

Becomes this on the terminal

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

This result was obtained like this

```
from Icon import Icon

if __name__ == '__main__':
    ic = Icon('/home/user/desktop/linkedin-logo.png', 15)
    print(ic)
```

## To use this in your project
**Leave a star**, download the Icon.py file, pip install the stuff on the imports, and use it as you would use any other class in your project.
