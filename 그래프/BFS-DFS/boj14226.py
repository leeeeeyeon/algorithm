import sys

input = sys.stdin.readline

s = int(input())

depth = 0
flag = False
result = [(1,0)]
st = set()

while True:
    temp = []

    depth += 1
    for screen, clip in result:
        if screen + clip == s or screen - 1 == s:
            flag = True
            break
        
        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if (screen, screen) not in st and screen != clip:
            temp.append((screen, screen))
            st.add((screen, screen))

        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if (screen+clip, clip) not in st:
            temp.append((screen+clip, clip))
            st.add((screen+clip, clip))

        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        if (screen-1, clip) not in st and screen > 0:
            temp.append((screen-1, clip))
            st.add((screen-1, clip))

    if flag:
        break

    result = temp

print(depth)