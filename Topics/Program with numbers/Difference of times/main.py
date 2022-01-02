# put your python code here
hour_01 = 3600 * int(input())
min_01 = 60 * int(input())
sec_01 = int(input())

hour_02 = 3600 * int(input())
min_02 = 60 * int(input())
sec_02 = int(input())

first = hour_01 + min_01 + sec_01
second = hour_02 + min_02 + sec_02

print(second - first)
