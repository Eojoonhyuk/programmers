# "*" 세로라인은 무조건 왼손, "#" 세로라인은 무조건 오른손
answer = ''
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]			
hand = "right"

def Distance(Current, Next):
  key_pad = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)
  }
  
  x1, y1 = key_pad[Current]
  x2, y2 = key_pad[Next]

  return abs(x1-x2) + abs(y1-y2)

left_hand_start = "*"
right_hand_start = "#"

for i in numbers:
  if i in [1, 4, 7]:
    answer += "L"
    left_hand_start = i
  elif i in [3, 6, 9]:
    answer += "R"
    right_hand_start = i
  elif i in [2, 5, 8, 0]:
    if Distance(left_hand_start, i) > Distance(right_hand_start, i):
      answer += "R"
      right_hand_start = i
    elif Distance(left_hand_start, i) < Distance(right_hand_start, i):
      answer += "L"
      left_hand_start = i
    else:
      if hand == "left":
        answer += "L"
        left_hand_start = i
      else:
        answer += "R"
        right_hand_start = i

print(answer)
