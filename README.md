# BlockCollisionsSimulator
Um simples programa em python (pygame) que simula colisões elásticas envolvendo dois blocos com massas diferentes

## Como funciona?

A classe "cube" gera um objeto "cubo", este possui massa, uma velocidade, e uma taxa de variação dessa velocidade, também chamada de aceleração.
Assim que dois cubos se tocam, a função "colision", definida em "Colision.py", através do principio de conservação do momentum linear, calcula a nova velocidade que os dois cubos terão.

## Fontes e interessantes

Esse vídeo do canal "3blue1brown" que me inspirou a criar o algorítimo
https://www.youtube.com/watch?v=HEfHFsfGXjs
Página da wikipédia sobre "momentum". Observe a parte sobre "colisões elásticas"
https://en.wikipedia.org/wiki/Momentum#Application_to_collisions
