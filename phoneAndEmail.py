import pyperclip,re


# Create a Regex for Phone Numbers

phoneRegex = re.compile(r'''(
        ([200~(\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''',re.VERBOSE)

# Create a Regex for Email Addresses

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
        )''',re.VERBOSE)


# Find All Matches in the Clipboard Text

text = str(pyperclip.paster())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+ groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
else:
        print('No phone numbers or email addresses found.')
