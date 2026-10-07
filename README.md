# Trigram Next-Word Predictor

## Overview

This project is a simple **trigram language model** that predicts the next word based on the previous two words.

The project was created as part of my Natural Language Processing coursework. It demonstrates how a basic language model can learn word patterns from a text dataset and use those patterns to make next-word predictions.

## How It Works

The program follows these main steps:

1. **Preprocess the text**
   - Converts all text to lowercase
   - Removes punctuation
   - Splits the text into individual words

2. **Build Trigram Counts**
   - Looks at three words at a time
   - Uses the first two words as the context
   - Counts how often each possible third word appears

3. **Calculate Probabilities**
   - Converts the word counts into probabilities
   - Higher probabilities mean the word appeared more often after that two-word context

4. **Predict the Next Word**
   - Takes two words as input
   - Returns the most likely words that come next

5. **Generate Text**
   - Starts with two words
   - Repeatedly predicts the most likely next word
   - Continues until the maximum length is reached or no prediction is available

## Example

For the context:

```text
i love
```

The model may learn that the following words are possible:

```text
natural
machine
learning
```

It then calculates the probability of each word and ranks them from highest to lowest.

Example output:

```text
Context: 'i love'

1. natural (0.500)
2. machine (0.250)
3. learning (0.250)
```

The text generation function can then use the highest-probability word to continue generating text.

## Technologies Used

- Python
- Regular Expressions (`re`)
- `string`
- `collections.defaultdict`
- `collections.Counter`

## Main Functions

### `preprocess_text()`

Cleans the training text by converting it to lowercase, removing punctuation, and creating a list of individual words.

### `build_trigram_counts()`

Creates trigram counts using two words as the context and the third word as the prediction.

### `build_trigram_probabilities()`

Converts the trigram counts into probabilities.

### `predict_next_words()`

Returns the top predicted next words for a given two-word context.

### `generate_text()`

Generates text by repeatedly selecting the highest-probability next word.

## What I Learned

Through this project, I learned how basic language models can use word patterns to predict what comes next in a sentence. I also practiced text preprocessing, dictionaries and counters in Python, probability calculations, and using functions to build a complete NLP workflow.

This project helped me understand the basic idea behind next-word prediction before moving on to more advanced NLP and neural network models.

## Running the Project

Make sure Python is installed on your computer.

Run the program with:

```bash
python trigram_language_model.py
```

The program will display:

- The processed tokens
- Trigram counts
- Trigram probabilities
- Next-word predictions
- Generated text

## Project Structure

```text
Trigram-Next-Word-Predictor/
│
├── trigram_language_model.py
└── README.md
```

## Author

**Noah Frami**

Natural Language Processing Coursework

October 2026
