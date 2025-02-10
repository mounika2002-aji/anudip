#1Q.Write a Python program to count the occurrences of each word in a given sentence
#the overall look of your document. To change the look available in the gallery” 

# Function to count the occurrences of each word in a sentence
def word_count(sentence):
    # Convert the sentence to lowercase and remove punctuation, then split into words
    sentence = sentence.lower().replace(".", "").replace(",", "").replace(":", "").replace(";", "")
    words = sentence.split()
    
    # Create a dictionary to store the word count
    word_dict = {}
    
    # Loop through each word and update the count in the dictionary
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Get the word count and print the result
word_counts = word_count(sentence)
print("Word occurrences:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
