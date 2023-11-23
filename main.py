from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.parsers.plaintext import PlaintextParser

# Specify the language for summarization (e.g., 'english', 'spanish', 'french', etc.)
language = "english"

# Define the URL to be summarized
article_url = ""

# Parse the HTML content of the URL
parser = HtmlParser.from_url(article_url, Tokenizer(language))

# Initialize the LsaSummarizer with the language-specific stop words
summarizer = LsaSummarizer(Stemmer(language))
summarizer.stop_words = get_stop_words(language)

# Summarize the URL content (e.g., 5 sentences in the summary)
num_sentences_in_summary = 9
url_summary = summarizer(parser.document, num_sentences_in_summary)

# Print the URL summary
print("URL Summary:")
for sentence in url_summary:
    print(sentence)

# Save the URL summary to a TXT file
url_summary_text = " ".join([str(sentence) for sentence in url_summary])
url_summary_file = "url_summary.txt"

# Open a file and write the summary to it
with open(url_summary_file, 'w', encoding='utf-8') as file:
    file.write(url_summary_text)
    
txt_file_path = "1.txt"
with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

# Initialize a PlaintextParser for text from a file
txt_parser = PlaintextParser.from_string(txt_content, Tokenizer(language))

# Summarize the TXT file content (e.g., 5 sentences in the summary)
txt_summary = summarizer(txt_parser.document, num_sentences_in_summary)
print("\nTXT File Summary:")
for sentence in txt_summary:
    print(sentence)

# Save the TXT file summary to a TXT file
txt_summary_text = " ".join([str(sentence) for sentence in txt_summary])
txt_summary_file = "txt_summary.txt"

# Open a file and write the summary to it
with open(txt_summary_file, 'w', encoding='utf-8') as file:
    file.write(txt_summary_text)


user_input = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
    ... Nunc in libero sit amet urna egestas varius.
"""

# Initialize a PlaintextParser for user input
user_parser = PlaintextParser.from_string(user_input, Tokenizer(language))

# Summarize the user input (e.g., 5 sentences in the summary)
user_summary = summarizer(user_parser.document, num_sentences_in_summary)
print("\nUser Input Summary:")
for sentence in user_summary:
    print(sentence)

# Save the user input summary to a TXT file
user_summary_text = " ".join([str(sentence) for sentence in user_summary])
user_summary_file = "user_summary.txt"

# Open a file and write the summary to it
with open(user_summary_file, 'w', encoding='utf-8') as file:
    file.write(user_summary_text)
