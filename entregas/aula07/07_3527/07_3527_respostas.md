Respostas - Atividade 07 - Matrícula 3527

Optei por usar a BFS (Breadth-First Search), além de eu estar mais acostumado e ter mais familiaridade com esse tipo de busca, sinto que nesse contexto para labirintos muito grandes poderia acabar tendo um problema de memória ou stackoverflow caso usasse um DFS por conta da sua estrutura que conta com uma pilha.

Outro motivo foi a expansão mais eficiente do BFS, no sentido de que é possível fazer labirintos com mais de um caminho e esse algoritmo irá encontrar o menor caminho. Por outro lado o DFS encontraria qualquer caminho baseado nas suas regras próprias. Na vida real costuma ser utilizado mais algoritmos pensando em encontrar o caminho mais eficiente, por tanto achei mais pertinente usar o BFS e não o DFS.

A depender do labirinto gerado e da posição do queijo, o BFS também pode ser mais eficiente - casos onde o queijo está a poucos passos de distância.
