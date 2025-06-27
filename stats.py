def count_words(contents):
    return len(contents.split())

def count_characters(contents):
    count = {}
    for char in contents.lower():
        count[char] = count.get(char, 0) +1
    return count

def return_item(item):
    return item["num"]

def sort_list(char_counts):
    transformed = [{"char": k, "num": v} for k, v in char_counts.items() if k.isalpha()]
    transformed.sort(reverse=True, key=return_item)
    return transformed