# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

#집합자료형
def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    
    lottos = set(lottos)
    win_nums = set(win_nums)
    
    high_score = len(lottos & win_nums) + zero
    low_score = len(lottos & win_nums)
    
    answer = [rank[high_score], rank[low_score]]
    return answer


# #5등
# if high_score == 2:
#     answer.insert(0, 5)
# if low_score == 2:
#     answer.insert(1, 5)
# #4등
# if high_score == 3:
#     answer.insert(0, 4)
# if low_score == 3:
#     answer.insert(1, 4)
# #3등
# if high_score == 4:
#     answer.insert(0, 3)
# if low_score == 4:
#     answer.insert(1, 3)
# #2등
# if high_score == 5:
#     answer.insert(0, 2)
# if low_score == 5:
#     answer.insert(1, 2)
# #1등
# if high_score == 6:
#     answer.insert(0, 1)
# if low_score == 6:
#     answer.insert(1, 1)
# #낙점
# if high_score == 1:
#     answer.insert(0, 6)
# if low_score == 1:
#     answer.insert(1, 6)
# if high_score == 0:
#     answer.insert(0, 6)
# if low_score == 0:
#     answer.insert(1, 6)

# print(answer)

