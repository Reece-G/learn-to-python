text = "X-DSPAM-confidence:    0.8475"
find = float(text[19:].strip())
print(find)
print(type(find))
