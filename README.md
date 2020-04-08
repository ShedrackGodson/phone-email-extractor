# phone-email-extractor
Say you have the boring task of finding every phone number and email
address in a long web page or document. If you manually scroll through
the page, you might end up searching for a long time. But if you had a pro-
gram that could search the text in your clipboard for phone numbers and
email addresses, you could simply press ctrl -A to select all the text, press
ctrl -C to copy it to the clipboard, and then run your program. It could
replace the text on the clipboard with just the phone numbers and email
addresses it finds.
# what it does
1. Get the text off the clipboard.
2. Find all the phone numbers and email addresses in the text document.
3. Paste them onto the clipboard.
4. Use the pyperclip module to copy ans paste the strings.
5. Create two regexes, one for matching phone numbers and the other for
matching email addresses.
6. Find all matches, not just the first match, of both regexes.
7. Neatly format the matched strings into a single string to paste.
8. Display some kind of message if no matches were found in the text.
