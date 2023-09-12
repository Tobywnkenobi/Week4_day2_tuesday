# Reverse all vowels in a string
# reverse_vowels('sean') => 'saen'
# reverse_vowels('dylan') => 'dalyn'
# reverse_vowels('lyla') => 'laly'
# reverse_vowels('heathir') => 'hiather

names = ["sean", "dylan", "lyla", "heathir", "raul", "porter", "toby"]

def reverse_vowels(l):
    vowels = "aeiouyAEIOUY"
    l = list(l)

    left, right = 0, len(l) - 1

    while left < right and l[left] not in vowels:
        left += 1

    while left < right and l[right] not in vowels:
        right -= 1

    l[left], l[right], = l[right], l[left]

    left += 1
    right -= 1

    return ''.join(l)

answer = {test: reverse_vowels(test) for test in names}
print(answer)

