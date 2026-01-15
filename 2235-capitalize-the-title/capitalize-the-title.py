class Solution(object):
    def capitalizeTitle(self, title):
        word = title.split()
        result = ""
        for i in word:
            if len(i) > 2:
                result += i.capitalize() + " "
            else:
                result += i.lower() + " "
        return result.strip()

