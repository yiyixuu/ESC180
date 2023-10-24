def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def first_last6(nums):
    return 6 == nums[0] or 6 == nums[-1]

def has23(nums):
    return 2 in nums or 3 in nums

def make_ends(nums):
    return [nums[0], nums[-1]]

def make_pi():
    return [3, 1, 4]

def max_end3(nums):
    return [max(nums[0], nums[2])]*3

def middle_way(a, b):
    return [a[1], b[1]]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def sum2(nums):
    return sum(nums[:2])

def sum3(nums):
    return sum(nums)

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def first_last6(nums):
    return 6 == nums[0] or 6 == nums[-1]

def has23(nums):
    return 2 in nums or 3 in nums

def make_ends(nums):
    return [nums[0], nums[-1]]

def make_pi():
    return [3, 1, 4]

def max_end3(nums):
    return [max(nums[0], nums[2])]*3

def middle_way(a, b):
    return [a[1], b[1]]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def sum2(nums):
    return sum(nums[:2])

def sum3(nums):
    return sum(nums)

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    return int(sum(sorted(nums)[1:-1]) / (len(nums)-2))

def count_evens(nums):
    return sum(1 for i in nums if i % 2 == 0)

def has22(nums): 
    return max([nums[i]==2 and nums[i+1]==2 for i in range(len(nums)-1)] + [False])

def sum13(nums):
    return sum([nums[i] for i in range(len(nums)) if nums[i] != 13 and (i == 0 or nums[i-1] != 13)])

def sum67(nums): 
    return (lambda l: sum([l[i] if l.index(7, i+1) < l.index(6, i) else 0 for i in range(len(nums))]))(nums[::-1] + [7,6])

def alarm_clock(day, vacation):
    return '7:00' if 1 <= day <= 5 and not vacation else '10:00' if not 1 <= day <= 5 and not vacation else '10:00' if 1 <= day <= 5 and vacation else 'off'

def caught_speeding(speed, is_birthday):
    return 0 if (is_birthday and speed <= 65) or (not is_birthday and speed <= 60) else 1 if (is_birthday and speed <= 85) or (not is_birthday and speed <= 80) else 2

def cigar_party(cigars, is_weekend):
    return (40<=cigars<=60 and not is_weekend) or (cigars >= 40 and is_weekend)

def date_fashion(you, date):
    return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1

def in1to10(n, outside_mode):
    return (n <= 1 or n >= 10) if outside_mode else (n >= 1 and n <= 10)

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

def sorta_sum(a, b):
    return 20 if 10 <= a + b <= 19 else a+b

def squirrel_play(temp, is_summer):
    return (60 <= temp <= 100 and is_summer) or (60 <= temp <= 90 and not is_summer)

def diff21(n):
    return abs(n - 21) if n <= 21 else 2 * abs(n - 21)

def front3(str):
    return str[:3] * 3

def front_back(str):
    return str if len(str) <= 1 else str[-1] + str[1:-1] + str[0]

def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10

def missing_char(str, n):
    return str.replace(str[n], '')

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

def not_string(str):
    return str if str[:3] == 'not' else "not " + str

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def pos_neg(a, b, negative):
    return a < 0 and b < 0 if negative else (a < 0 and b > 0) or (a > 0 and b < 0)

def sleep_in(weekday, vacation):
    return not weekday or vacation

def sum_double(a, b):
    return 2 * (a + b) if a == b else a + b

def array_count9(nums):
    return sum([1 for i in nums if i == 9])

def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    return 1 and 2 and 3 in nums

def front_times(str, n):
    return str[:3] * n

def last2(str):
    return sum([1 for i in range(len(str) - 2) if str[i:i + 2] == str[-2:]])

def string_bits(str):
    return str[::2]

def string_match(a, b):
    return sum([1 for i in range(min(len(a), len(b)) - 1) if a[i:i+2] == b[i:i+2]])

def string_times(str, n):
    return str * n

def string_splosion(str):
    return ''.join([str[:i] for i in range(1, len(str) + 1)])