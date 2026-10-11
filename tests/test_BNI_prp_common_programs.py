#Check Palindrome , ignore case
import pytest
# with parameterzed fixture
import pytest

def is_palindrome(word):
    mod_word = word.lower()
    return mod_word == mod_word[::-1]


print(is_palindrome("kanchan"))

@pytest.mark.parametrize("word ,expected", [("madam" , True),("Madam" , True) ,("a" , True),("kanchan" , False)])
def test_palindrome(word , expected):
    assert is_palindrome(word) == expected 

# without parameterized, single input

def is_palindrome(word):
    mod_word = word.lower()
    return mod_word == mod_word[::-1]


def test_palindrome():
    assert is_palindrome("Madam") == True 


# Count vowels, ignoring case

import pytest

def check_vowels(s):
    vowels ='aeiouAEIOU'
    count = 0
    for ch in s:
        if ch in vowels:
            count = count +1
    return count


@pytest.mark.parametrize("s,expected_vow_count",[("" , 0), ("xyz" ,0), ("AEIOU",5)])
def test_check_vowels(s, expected_vow_count):
    assert check_vowels(s) == expected_vow_count , f'{s}'


# Same letters, ignoring case and spaces

def is_anagram(a, b):
    return sorted(a) == sorted(b)


def test_is_anagram():
    assert is_anagram("madam","madam") == True
    assert is_anagram("Dormitory","Dirty Room") == False


# remove_duplicates(lst)

import pytest

def remove_duplicate(lst):
    non_dup = []
    for num in lst:
        if num not in non_dup:
            non_dup.append(num)
    return non_dup


@pytest.mark.parametrize("lst,expected" ,[([], []),([1,1,1] ,[1]), ([2,3,4,5,1,3] ,[2,3,4,5,1]),([1,2,2,3,1],[1,2,3])])
def test_remove_duplicate(lst,expected):
    assert remove_duplicate(lst) == expected


# Return a dict of counts , character frequency

import pytest
def count_char_freq(word):
    char_freq = {}
    for ch in word :
        char_freq[ch] = char_freq.get(ch,0) +1
    return char_freq


@pytest.mark.parametrize("char,expected", [("kanchan",{"k":1,"a":2,"n":2,"c":1,"h":1})])
def test_count_char_freq(char , expected):
    assert count_char_freq(char) == expected


# A function return_list that takes a number n and returns all numbers from 1 to n in one list.

# Input: one number n
# Output: a list, not a single number

def show_list_upto_n(n):
    final_list=[]
    for i in range(1, n+1):
        final_list.append(i)
    return final_list

@pytest.mark.parametrize("n,expected",[(3,[1,2,3]) , (4,[1,2,3,4]) , (3,[1,2,3])])
def test_show_list_upto_n(n, expected):
    assert show_list_upto_n(n) == expected ,f"{n} not matched"


#Sum of the digits


def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    return sum


@pytest.mark.parametrize("n,expected",[(15, 6),(125,8) ,(4892 , 23)])
def test_sum_of_digits(n,expected):
    assert sum_of_digits(n) == expected






