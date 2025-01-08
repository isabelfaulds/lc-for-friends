#### Rolling Hash
- Rabin-Karp Algorithm, 1987, "Efficient Randomized Pattern-Matching Algorithms"
- ❎ not ideal for short strings
- ❎ limited input size
- ✅ long string sizes
- ✅ scalable input size
- precompute hash values for all prefixes & suffixes in o(n * k)
- access computed hash values in o ( 1 )

