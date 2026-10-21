class Solution:

    def encode(self, strs: List[str]) -> str:
        # secretS = ""
        # for st in strs:
        #     for c in st:
        #         secretS += str(ord(c)) + '+'
        #     secretS += '-'
        # return secretS
        # print(len(strs))
        if len(strs) == 0:
            return ""
        return "1!@/" + "!@/".join(strs)

    def decode(self, s: str) -> List[str]:
        # listStr = s.split('-')
        # decodeSt = []
        # for i in range(0, len(listStr)-1):
        #     charList = listStr[i].split('+')
        #     decodeSt.append("")
        #     for c in charList[0:len(charList)-1]:
        #         decodeSt[i] += chr(int(c))
        # return decodeSt
        # print(s)
        if s == "":
            return []
        decode = s.split("!@/")
        return decode[1:]