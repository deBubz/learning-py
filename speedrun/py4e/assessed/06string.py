# prints out the number
text = "X-DSPAM-Confidence:    0.8475"

i = text.find("0")
x = float(text[i:])
print(x)