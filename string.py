""" Worked Solution 1: Three-String Transformation
Problem: Given three strings as input, apply separate transformations to each: replace vowels with # in the first string, replace consonants with * in the second string, convert all characters to uppercase in the third string.
Sample input: s1 = FACEPREP, s2 = hello, s3 = world
Expected output: F#C#PR#P / *e**o / WORLD """
#Code
#Python :
def transform_strings(s1, s2, s3):
    res1 = ""
    res2 = ""
    
    # 1. Replace vowels in s1
    for i in s1:
        if i in "AEIOUaeiou":
            res1 += "#"
        else:
            res1 += i
            
    # 2. Replace consonants in s2
    for i in s2:
        if i in "AEIOUaeiou":
            res2 += i
        else:
            res2 += "*"
            
    # 3. Uppercase s3
    res3 = s3.upper()
    
    # Format and return using string formatting or join
    return f"{res1} / {res2} / {res3}"

# Sample execution
print(transform_strings("FACEPREP", "hello", "world"))


# Output: F#C#PR#P / *e**o / WORLD
