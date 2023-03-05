def solution(wallpaper):
    answer = []
    
    files_x = []
    files_y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                files_x.append(i)
                files_y.append(j)

    return [min(files_x), min(files_y), max(files_x)+1, max(files_y)+1]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))