sx, sy, tx, ty = map(int, input().split())

move_y = ty-sy
move_x = tx-sx

ans = ''
ans += 'U'*move_y + 'R'*move_x
ans += 'D'*move_y + 'L'*move_x
ans += 'L' + 'U'*move_y + 'U' + 'R'*move_x + 'R' + 'D'
ans += 'R' + 'D'*move_y + 'D' + 'L'*move_x + 'L' + 'U'

print(ans)