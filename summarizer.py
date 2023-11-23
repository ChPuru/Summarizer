from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_text_with_sumy(text, language, ratio=0.2):
    """
    Summarizes a piece of text using the LsaSummarizer from sumy.

    Args:
        text (str): The text to be summarized.
        language (str): The language of the text (e.g., 'english', 'spanish', 'french', etc.).
        ratio (float): The ratio of the original text to include in the summary (default is 0.2).

    Returns:
        str: The summarized text.
    """
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summarizer = summarizer(parser.document, ratio=ratio)

    summary = ""
    for sentence in summarizer:
        summary += str(sentence) + " "

    return summary


def save_summary_to_txt(summary, output_file_path):
    """
    Saves a summary to a TXT file.

    Args:
        summary (str): The summary text.
        output_file_path (str): The path to the output TXT file.
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)
