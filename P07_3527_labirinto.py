from collections import deque
# importando o deque para aumentar a perfomance 

def bfs(maze, wall, cheese):
    m, n = len(maze), len(maze[0])
    start = (1,1)
    queue = deque([start])  # variáveis ambiente
    visited = set()
    parent = { start: None }

    while len(queue):
        x,y = queue.popleft() 
        visited.add((x,y))

        # caso encontre o queijo
        # reconstrua o caminho usando os parents
        if maze[x][y] == cheese:
            path = []
            pos = (x, y)
            while pos is not None:
                path.append(pos)
                pos = parent[pos]
            return path

        # percorre esquerda direita baixo e em cima para procurar e adiciona a fila as próximas buscas
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx,ny = x + dx, y + dy
            # se nao é parede e está dentro dos limites, adiciona a fila
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != wall and (nx, ny) not in visited:
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return False

# printa o resultado final do caminho
def print_bfs(maze, path):
    maze_copy = [ row.copy() for row in maze ]
    for x, y in path[1:]:
        maze_copy[x][y] = "-"

    for row in maze_copy:
        print(" ".join(map(str, row)))
## -- ##

# um teste padrão randômico
from maze_builder import generate_maze

if __name__ == '__main__':
    m, n = 10, 14
    room = ' '
    wall = 'W'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    path = bfs(maze, wall, cheese)
    print_bfs(maze,path)