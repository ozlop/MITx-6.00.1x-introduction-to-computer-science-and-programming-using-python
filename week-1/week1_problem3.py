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

