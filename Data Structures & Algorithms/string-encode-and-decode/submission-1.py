class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =""
        for word in strs:
            encoded += str(len(word)) + "#"+ word
        
        return encoded 

    def decode(self, encoded: str) -> List[str]:
        result = []

        i = 0

        while i < len(encoded):
            j = i

            # Find the separator after the length.
            while encoded[j] != "#":
                j += 1

            length = int(encoded[i:j])
            i = j + 1

            result.append(encoded[i:i + length])
            i += length

        return result
