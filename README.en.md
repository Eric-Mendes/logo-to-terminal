# logo-to-terminal
Show a black and white Icon as text on terminal.

## Motivation
Back-end doesn't have to be *visually* "uniteresting". With that in mind (and also inpired by [this](https://www.hackerrank.com/challenges/text-alignment/problem "See the problem") Hackerrank problem) I created this code.

## How it works
Using [PIL](https://pillow.readthedocs.io/en/stable/ "Read the docs") to deal with the images and [numpy](https://numpy.org/ "Go to numpy's website") to turn them into a 2D array of integers, this code maps the color black (255) to the symbol \# and the color white (0) to a whitespace.

## To run
To run this you install all the stuff on the imports and run it as a usual python. For example:
```
python3 main.py
```

## For the future...
My intention is to turn this into a lib so anyone can use this in their code.
