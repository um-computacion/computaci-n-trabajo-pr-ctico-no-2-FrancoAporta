import re

def is_palindrome(text):
    
    text = text.lower()

    cleaned_text = re.sub(r'[^a-z0-9]', '', text)

    return cleaned_text == cleaned_text[::-1]