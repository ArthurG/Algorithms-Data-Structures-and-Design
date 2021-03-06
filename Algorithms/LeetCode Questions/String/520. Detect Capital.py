'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if (word == ""):
            return True

        startLetter = word[0]
        secondLetter = None
        if len(word) == 1 and startLetter.isupper():
            return True
        elif len(word) > 1:
            secondLetter = word[1]

        if (startLetter.isupper()):  # Second letter only matters when the startLetter is capital
            if (secondLetter.isupper()):
                # All letters must be caps or false
                for i in range(2, len(word)):
                    if (word[i].islower()):
                        return False
                return True
            else:
                # First letter is uppercase and there are more letters and lowercase
                for i in range(2, len(word)):
                    if (word[i].isupper()):
                        return False
                return True

        else:
            # all must be lower case

            for i in range(1, len(word)):
                if (word[i].isupper()):
                    return False
            return True

    #FASTER

    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            if word.isupper() or word.islower():
                return True
            elif word.istitle():
                return True
            else:
                return False