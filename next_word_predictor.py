"""
Trigram Next-Word Predictor - Starter Template
Name: Noah Frami
Date: 10/7/2026
"""

import string
from collections import defaultdict, Counter


def preprocess_text(text):
    """
    Convert text to lowercase, remove punctuation, and split into tokens.
    """
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into tokens
    tokens = text.split()

    return tokens


def build_trigram_counts(tokens):
    """
    Build trigram counts in the form:
    (word1, word2) -> Counter({next_word: count})
    """
    trigram_counts = defaultdict(Counter)

    # Loop through tokens and count trigrams
    for i in range(len(tokens) - 2):
        context = (tokens[i], tokens[i + 1])
        next_word = tokens[i + 2]
        trigram_counts[context][next_word] += 1

    return trigram_counts


def build_trigram_probabilities(trigram_counts):
    """
    Convert trigram counts into probabilities.
    Returns:
    (word1, word2) -> {next_word: probability}
    """
    trigram_probs = {}

    # Loop through each context in trigram_counts
    # Find total count for that context
    # Compute probabilities for each next word
    for context, next_words in trigram_counts.items():
        total_count = sum(next_words.values())
        trigram_probs[context] = {}

        for word, count in next_words.items():
            trigram_probs[context][word] = count / total_count

    return trigram_probs


def predict_next_words(word1, word2, trigram_probs, top_n=3):
    """
    Return the top N most likely next words for the given two-word context.

    Example return value:
    [("natural", 0.5), ("machine", 0.25), ("learning", 0.25)]
    """
    context = (word1.lower(), word2.lower())

    # Return empty list if context is not found
    if context not in trigram_probs:
        return []

    # Convert predictions to a list of tuples
    predictions = list(trigram_probs[context].items())

    # Sort by probability, highest first
    predictions.sort(key=lambda item: item[1], reverse=True)

    # Return top_n items
    return predictions[:top_n]


def generate_text(start_words, trigram_probs, max_length=10):
    """
    Generate text by repeatedly choosing the highest-probability next word.

    start_words should contain exactly two words.
    """
    words = start_words.lower().split()

    # Check that exactly two start words were given
    if len(words) != 2:
        return "Error: Please provide exactly two starting words."

    generated = words[:]

    # Repeatedly predict and append the next word
    for _ in range(max_length):
        # Define the context
        context = (generated[-2], generated[-1])
        # Stop if the context is not found
        if context not in trigram_probs:
            break

        next_word_probs = trigram_probs[context]
        next_word = max(next_word_probs, key=next_word_probs.get)
        generated.append(next_word)


    return " ".join(generated)


def print_trigram_counts(trigram_counts):
    """
    Print trigram counts in a readable way.
    """
    print("\nTrigram Counts:")
    for context, counter in trigram_counts.items():
        print(f"{context} -> {dict(counter)}")


def print_trigram_probabilities(trigram_probs):
    """
    Print trigram probabilities in a readable way.
    """
    print("\nTrigram Probabilities:")
    for context, prob_dict in trigram_probs.items():
        print(f"{context} -> {prob_dict}")


def main():
    text = """
    I love natural language processing.
    I love machine learning.
    Natural language processing is fun.
    Machine learning is powerful.
    I love learning new things.
    I love natural language models.
    Natural language models are useful.
    """

    # Step 1: Preprocess text
    tokens = preprocess_text(text)

    print("Tokens:")
    print(tokens)

    # Step 2: Build trigram counts
    trigram_counts = build_trigram_counts(tokens)
    print_trigram_counts(trigram_counts)

    # Step 3: Build trigram probabilities
    trigram_probs = build_trigram_probabilities(trigram_counts)
    print_trigram_probabilities(trigram_probs)

    # Step 4: Test next-word prediction
    print("\nTop 3 Next-Word Predictions:")

    test_contexts = [
        ("i", "love"),
        ("natural", "language"),
        ("machine", "learning"),
    ]

    for word1, word2 in test_contexts:
        predictions = predict_next_words(word1, word2, trigram_probs, top_n=3)
        print(f"\nContext: '{word1} {word2}'")

        if not predictions:
            print("No predictions found.")
        else:
            for i, (word, prob) in enumerate(predictions, start=1):
                print(f"{i}. {word} ({prob:.3f})")

    # Step 5: Generate text
    print("\nGenerated Text:")
    prompts = [
        "i love",
        "natural language",
        "machine learning"
    ]

    for prompt in prompts:
        generated = generate_text(prompt, trigram_probs, max_length=8)
        print(f"Prompt: '{prompt}'")
        print(f"Generated: {generated}")
        print("-" * 50)


if __name__ == "__main__":
    main()