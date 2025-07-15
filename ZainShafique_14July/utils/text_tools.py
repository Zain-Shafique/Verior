from collections import Counter

def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    
    words = text.lower().split()
    word_freq = Counter(words)
    most_frequent = word_freq.most_common(1)[0][0] if words else None
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'most_frequent': most_frequent
    }