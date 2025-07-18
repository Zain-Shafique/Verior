from textblob import TextBlob
import pandas as pd

def get_sentiment_category(polarity: float) -> str:
    """Categorize sentiment based on polarity score."""
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiments(sentences: list) -> None:
    """
    Task 01: Print each sentence with its polarity and sentiment.
    Args:
        sentences: List of text strings to analyze.
    """
    for sentence in sentences:
        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity
        sentiment = get_sentiment_category(polarity)
        print(f"Sentence: {sentence}")
        print(f"Polarity: {polarity:.4f}")
        print(f"Sentiment: {sentiment}\n")

def analyze_csv(input_path: str, output_path: str, text_column: str = "Tweet") -> None:
    """
    Task 02: Analyze sentiment for text in a CSV column and save results.
    Args:
        input_path: Path to input CSV file.
        output_path: Path to save the output CSV.
        text_column: Name of the column containing text (default: "Tweet").
    """
    # Read CSV file with proper encoding
    try:
        df = pd.read_csv(input_path, encoding='cp1252')
    except UnicodeDecodeError:
        # Fallback to latin1 if cp1252 fails
        df = pd.read_csv(input_path, encoding='latin1')
    
    # Ensure text_column exists
    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in the CSV file.")
    
    # Process each row
    def analyze_row(row):
        text = str(row[text_column])
        try:
            blob = TextBlob(text)
        except:
            # Handle encoding issues in text
            cleaned_text = text.encode('ascii', 'ignore').decode('ascii')
            blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        return polarity, get_sentiment_category(polarity)
    
    # Apply analysis and create new columns
    df[['Polarity', 'Sentiment']] = df.apply(
        lambda row: analyze_row(row), 
        axis=1, 
        result_type='expand'
    )
    
    # Save to new CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Results saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Task 01 Demo
    sample_sentences = [
        "I love this product!",
        "This is terrible.",
        "The weather is okay today."
    ]
    print("Task 01 Results:\n" + "="*40)
    analyze_sentiments(sample_sentences)
    
    # Task 02 - Process twitter.csv
    analyze_csv("twitter.csv", "twitter_with_sentiment.csv")
