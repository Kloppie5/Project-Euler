
def digit_to_english(n) :
    assert 10 > n and n >= 0
    return [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ][n]

def thousands_to_english(n) :
    assert 1000 > n and n >= 0

    if n == 0 :
        return "zero"
    
    s = ""

    hundreds = n // 100
    tens = n % 100 // 10
    digit = n % 10

    if hundreds > 0 :
        s += f"{digit_to_english(hundreds)} hundred"
        if tens + digit > 0 :
            s += " and "

    if tens == 1 :
        s += [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen"
        ][digit]
        return s

    if tens > 1 :
        s += [
            "-",
            "-",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety"
        ][tens]
        if digit > 0 :
            s += "-"
    
    if digit > 0 :
        s += digit_to_english(digit)
    
    return s

def number_to_english(n) :
    assert 10**24 > n and n >= 0
    
    if n == 0 :
        return "zero"
    
    segments = []
    segment_names = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion",
        "quintillion",
        "sextillion"
    ]
    while n > 0 :
        segments.append(thousands_to_english(n % 1000))
        n //= 1000
    
    s = " "
    for i in range(len(segments)-1, -1, -1) :
        if segments[i] != "zero" :
            s += f"{segments[i]} {segment_names[i]} "
    return s[:-1]


print(
    sum(
        [
            len(number_to_english(i).replace(' ', '').replace('-', ''))
            for i in range(1, 1001)
        ]
    )
)