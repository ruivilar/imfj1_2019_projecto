# __Projeto Final__ 
Afonso Lage - a21901381 - (git) AfonsoLage-boop  
André Santos - a21901767 - (git) andrepucas  
Rui Vilar - a21902960 - (git) ruivilar
</br>

__Grupo:__ Iniciados
</br>

---
## __Observação Inicial__
Neste trabalho nós fizemos o visualiser na totalidade onde decidimos trocar os dois quadrados por duas pirâmides (uma grande cor de rosa e uma do tipo child, branca).

A grande maioria dos controlos do visualizer foram implementados por Afonso Lage (rotação e translação) e a substituição dos objetos por pirâmides foram feitas por André Santos. O Rui iniciou o desenvolvimento do FPS. 

O FPS foi a parte que ficou mais incompleta, onde temos apenas alguns controlos basicos e objetos.  

__Nota:__ Nós trocamos o nome do sample.py para visualizer.py e criámos uma cópia do visualizer para trabalhar no fps-like.py
</br></br>

---


## Controlos do visualizer: 
Para fazer esta parte foram criados vários ifs que sempre que o jogador carrega na tecla de movimento redefinem o angulo, o vetor  e normalizam esse vetor. 

Depois reutilizámos a equação que estava a ser usada para a rotação automática dos objetos para condizer com o que precisávamos.

Para o movimento dos objetos simplesmente foi somado um vetor que move o objeto na direção desejada.

## Novos objetos no visualizer: 
Para a criação de novos objetos foi preciso criar também novas funções no módulo mesh.py entre as quais: __create_pyramid__
e __create_triangle__  .

Ambas muito semelhantes e inspiradas nas funções usadas para a criação dos cubos.

Para fazer então a pirâmide foi reutilizada uma das faces do cubo (a de baixo, criada na função __create_quad__) e criados dois triangulos com a função __create_triangle__.

Colocar os triângulos nas posições certas e descobrir quais os appends para juntar os vertices foi um desafio que acabou por ser facilitado quando percebemos que só precisávamos de dois triângulos e de uma base para fazer uma pirâmide apenas com arestas.

## FPS-like:
Fizemos uma aproximação de uma _reticle_ (visto que é um FPS) e preenchemos também o cenário.

Alterámos também os movimentos (provenientes do visualizer) para corresponder a controlos WASD de um FPS. Estas modificações encontram se comentadas no código.

</br>

---
## __PostMortem__

Neste projeto houve mais coisas a correrem mal do que bem, especialmente na parte do fps, que começámos bastante à ultima da hora para o que é.

No visualizer o maior problema foi descobrir como é que os appends que formam as faces funcionavam (foi gasto algum papel para descobrir o que estava a acontecer). Depois de percebido, atribuir as somas de vetores necessárias para que os triângulos ficassem na posição certa tornou-se muito mais facil.

Um problema recorrente no fps foi a tentativa de fazer o jogador virar-se. A nossa primeira hipotese para resolver isto consistia em detetar onde estava o mouse no ecrâ e depois mexer os objetos para a esquerda ou direita. Para além da nossa implementação funcionar mal, era também deselegante.
</br>




