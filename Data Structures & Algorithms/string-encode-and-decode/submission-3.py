class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded_st = ""
            for char in st:
                
                encoded_st += chr(ord(char)+1)
            
            encoded += "*#" + encoded_st
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        encoded = s.split("*#")[1:]
        decoded = []
        for st in encoded:
            decoded_st = ""
            for char in st:
                decoded_st += chr(ord(char)-1)

            decoded.append(decoded_st)

        return decoded