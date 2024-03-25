#명령어
###################################################
# 파이선의 배열은 리스트, 튜플, 문자열, 셋, 딕셔너리가 있다.

# String.join(변수값 for 변수값 in list)


# 문자열을 연결하는 함수
list = ["테스트", "준비", "완료"]

#Join 리스트 형태의 각 값을 특정 문자로 연결해준다.
print(' '.join(변수값 for 변수값 in list))
# 실행결과 : 테스트 준비 완료

print(''.join(변수값 for 변수값 in list))
# 실행결과 : 테스트준비완료

#문자열에서 특정 문자 찾기 => index
print("string".find('r'))
###################################################

