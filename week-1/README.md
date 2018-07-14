### Week 1
---

#### Problem 1
Assume `s` is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: '`a`', '`e`', '`i`', '`o`', and '`u`'. For example, if `s = 'azcbobobegghakl'`, your program should print:

`Number of vowels: 5`


```python
s = 'azcbobobegghakl'
vowels = 0


for letter in s:
  if letter == 'a' or letter == 'e' or letter == 'i' or \
     letter == 'o' or letter == 'u':
    vowels += 1
print("Number of vowels: " + str(vowels))
```

    Number of vowels: 5

<br>


#### Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string `'bob'` occurs in `s`. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Number of times bob occurs is: 2`


```python
s = 'azcbobobegghakl'
count = 0
matched = 0
target = 'bob'


for check in s:
    string = s[count:count+3]
    if string == target:
        matched +=1
    count += 1

print("Number of times bob occures is: " + str(matched))
```

    Number of times bob occurs is: 2

<br>


### Problem 3
Assume `s` is a string of lower case characters.

Write a program that prints the longest substring of `s` in which the letters occur in alphabetical order. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`, then your program should print

`Longest substring in alphabetical order is: abc`


```python
s = 'dhasoovwcihmindnrcgooy'
check = s[0]
done = s[0]


for letter in range(1,len(s)):
    if s[letter] >= check[len(check)-1]:
        check += s[letter]
    if s[letter] < check[len(check)-1]:
        if len(check) > len(done):
            done = check
        if len(check) == len(done):
            pass
        check = s[letter]


if len(check) > len(done):
    done = check

print("Longest substring in alphabetical order is: "+ done)
```

    Longest substring in alphabetical order is: cgooy
