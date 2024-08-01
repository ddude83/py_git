# !usr/bin/python3

import re

import pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
 (\S|-)       # first separator
 \d\d\d       # first 3 digits
 -       # separator
\d\d\d\d     # last 4 digits
(((ext(\.)?\s)|x)      # extension word-part (optional)
(\d{2,5}))?       # extension number-part (optional)
)
''', re.VERBOSE)
# Create a regex for email addresses

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name part

''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from this text

exctractedPhone = phoneRegex.findall(text)
exctractedEmail = emailRegex.findall(text)

allPhonenumbers = []
for phoneNumber in exctractedPhone:
    allPhonenumbers.append(phoneNumber[0])

print(exctractedPhone)
print(exctractedEmail)
# Copy the extracted email/ phone ti the clipboard
