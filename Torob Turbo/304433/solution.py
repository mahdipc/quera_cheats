class WordAnalogy:
    def run(self, input):
        import numpy as np
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        from sklearn.decomposition import TruncatedSVD
        from collections import defaultdict
        import re

        corpus = []
        word_pairs = []
        analogy_dict = defaultdict(dict)

        try:
            with open("word-analogy-train.txt", "r", encoding="utf-8") as f:
                current_category = ""
                for line in f:
                    line = line.strip()
                    if line.startswith(":"):
                        current_category = line[1:].strip()
                    elif line:
                        parts = line.split()
                        if len(parts) == 4:
                            w1, w2, w3, w4 = parts
                            # Store analogies for direct lookup
                            analogy_dict[(w1, w2, w3)] = w4
                            analogy_dict[(w3, w4, w1)] = w2
                            # Collect words for corpus
                            corpus.extend([w1, w2, w3, w4])
                            word_pairs.append((w1, w2))
                            word_pairs.append((w3, w4))
        except:
            pass

        # Build word embeddings using co-occurrence matrix
        class SimpleWordEmbedding:
            def __init__(self, window_size=5, vector_size=100):
                self.window_size = window_size
                self.vector_size = vector_size
                self.word_to_idx = {}
                self.idx_to_word = {}
                self.embeddings = None

            def fit(self, words):
                # Build vocabulary
                unique_words = list(set(words))
                self.word_to_idx = {word: idx for idx, word in enumerate(unique_words)}
                self.idx_to_word = {idx: word for word, idx in self.word_to_idx.items()}
                vocab_size = len(unique_words)

                # Build co-occurrence matrix
                cooc_matrix = np.zeros((vocab_size, vocab_size))

                # Count co-occurrences from word pairs and sequences
                for i in range(len(words) - 1):
                    if (
                        words[i] in self.word_to_idx
                        and words[i + 1] in self.word_to_idx
                    ):
                        idx1 = self.word_to_idx[words[i]]
                        idx2 = self.word_to_idx[words[i + 1]]
                        cooc_matrix[idx1, idx2] += 1
                        cooc_matrix[idx2, idx1] += 1

                # Add smoothing
                cooc_matrix = cooc_matrix + 0.1

                # Apply TF-IDF weighting
                from sklearn.feature_extraction.text import TfidfTransformer

                tfidf = TfidfTransformer()
                cooc_matrix = tfidf.fit_transform(cooc_matrix).toarray()

                # Reduce dimensions using SVD
                if vocab_size > self.vector_size:
                    svd = TruncatedSVD(
                        n_components=min(self.vector_size, vocab_size - 1)
                    )
                    self.embeddings = svd.fit_transform(cooc_matrix)
                else:
                    self.embeddings = cooc_matrix

                # Normalize embeddings
                norms = np.linalg.norm(self.embeddings, axis=1, keepdims=True)
                norms[norms == 0] = 1
                self.embeddings = self.embeddings / norms

            def get_vector(self, word):
                if word in self.word_to_idx:
                    return self.embeddings[self.word_to_idx[word]]
                elif word.lower() in self.word_to_idx:
                    return self.embeddings[self.word_to_idx[word.lower()]]
                else:
                    # Return average vector for unknown words
                    return np.mean(self.embeddings, axis=0)

            def most_similar(self, positive=[], negative=[], topn=1):
                # Calculate target vector
                target = np.zeros(self.embeddings.shape[1])
                for word in positive:
                    target += self.get_vector(word)
                for word in negative:
                    target -= self.get_vector(word)

                # Normalize
                norm = np.linalg.norm(target)
                if norm > 0:
                    target = target / norm

                # Calculate similarities
                similarities = cosine_similarity([target], self.embeddings)[0]

                # Exclude input words
                exclude = set(positive + negative)
                exclude.update([w.lower() for w in exclude])

                # Find top matches
                results = []
                indices = np.argsort(similarities)[::-1]
                for idx in indices:
                    word = self.idx_to_word[idx]
                    if word not in exclude and len(results) < topn:
                        results.append((word, similarities[idx]))

                return results

        # Create and train embedding model
        model = SimpleWordEmbedding(window_size=3, vector_size=50)
        if corpus:
            model.fit(corpus)

        def solve_analogy(w1, w2, w3):
            """Solve analogy: w1:w2 :: w3:?"""

            # First check direct lookup
            if (w1, w2, w3) in analogy_dict:
                return analogy_dict[(w1, w2, w3)]

            # Try with embeddings if we have them
            if model.embeddings is not None:
                try:
                    results = model.most_similar(
                        positive=[w2, w3], negative=[w1], topn=1
                    )
                    if results:
                        return results[0][0]
                except:
                    pass

            # Fallback to rule-based approach
            return apply_rules(w1, w2, w3)

        def apply_rules(w1, w2, w3):
            """Apply linguistic rules as fallback"""

            # Check for suffix/prefix patterns
            if len(w2) > len(w1) and w2.startswith(w1):
                suffix = w2[len(w1) :]
                return w3 + suffix
            elif len(w2) > len(w1) and w2.endswith(w1):
                prefix = w2[: -len(w1)]
                return prefix + w3

            # Check for common transformations
            # Past tense
            if w2.endswith("ed") and not w1.endswith("ed"):
                if w3.endswith("e"):
                    return w3 + "d"
                elif w3.endswith("y") and w3[-2] not in "aeiou":
                    return w3[:-1] + "ied"
                else:
                    return w3 + "ed"

            # Plural
            if w2.endswith("s") and not w1.endswith("s"):
                if w3.endswith("y") and w3[-2] not in "aeiou":
                    return w3[:-1] + "ies"
                elif w3.endswith(("s", "x", "z", "sh", "ch")):
                    return w3 + "es"
                else:
                    return w3 + "s"

            # Present participle
            if w2.endswith("ing") and not w1.endswith("ing"):
                if w3.endswith("e") and not w3.endswith("ee"):
                    return w3[:-1] + "ing"
                else:
                    return w3 + "ing"

            # Comparative
            if w2.endswith("er") and not w1.endswith("er"):
                if w3 == "good":
                    return "better"
                elif w3 == "bad":
                    return "worse"
                elif w3.endswith("y"):
                    return w3[:-1] + "ier"
                else:
                    return w3 + "er"

            # Superlative
            if w2.endswith("est") and not w1.endswith("est"):
                if w3 == "good":
                    return "best"
                elif w3 == "bad":
                    return "worst"
                elif w3.endswith("y"):
                    return w3[:-1] + "iest"
                else:
                    return w3 + "est"

            # Adverb
            if w2.endswith("ly") and not w1.endswith("ly"):
                if w3.endswith("y"):
                    return w3[:-1] + "ily"
                elif w3.endswith("le"):
                    return w3[:-1] + "y"
                else:
                    return w3 + "ly"

            # Default: return as is
            return w3

        # Process test data
        results = []

        for row in input:
            if len(row) >= 4:
                category = row[0]
                word1 = row[1]
                word2 = row[2]
                word3 = row[3]

                # Skip category headers
                if category.startswith(":"):
                    continue

                # Solve the analogy
                word4 = solve_analogy(word1, word2, word3)

                results.append({"category": category, "word4": word4})

                print(f"Processed: {word1}:{word2}::{word3}:{word4}")

        # Save results
        df = pd.DataFrame(results)
        df.to_csv("submission.csv", index=False)
        print(f"\nGenerated submission.csv with {len(results)} predictions")

        return df
