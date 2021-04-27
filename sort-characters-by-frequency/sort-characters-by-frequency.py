class Solution:
    def frequencySort(self, s: str) -> str:
        # Count up the occurances.
        counts = dict(collections.Counter(s))
        # Build up the string builder.
        string_builder = []
        sortedCountsKey = sorted(counts, key=lambda x: counts[x], reverse=True)
        for letter in sortedCountsKey:
            # letter * freq makes freq copies of letter.
            # e.g. "a" * 4 -> "aaaa"
            string_builder.append(letter * counts[letter])
        return "".join(string_builder)