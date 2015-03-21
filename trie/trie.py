class Trie(object):

    def __init__(self):
        # next is a dict mapping characters to the nodes that contain
        # that subtrie
        self.nexts = {}

    def as_string(self, inchar="", depth=0):
        """return pretty string representing the trie: show char for a node
and then, one character over, the subtrie of every character in the .nexts
dict, with blank line for root, e.g. [hi, ho] as:

h
-i
-o
        """
        # Create a global state *shudder* if it doesn't exist
        global glbst
        try:
            glbst
        except NameError:
            glbst = []
        # keep appending the lines to it
        glbst.append("{lead}{char}".format(
            lead=depth*"-",
            char=inchar,
        ))
        for key, val in self.nexts.iteritems():
            val.as_string(key, depth + 1)
        # return the line-delimited string that joins them
        return "\n".join(glbst)

    def has_key(self, word):
        """returns True if word in trie, False otherwise
        """
        if len(word) == 0:
            return True
        elif word[0] in self.nexts:
            return self.nexts[word[0]].has_key(word[1:])
        else:
            return False

    def insert(self, word):
        # if empty, we're done
        if len(word) == 0:
            return
        # if first char in next dict, descend there with the word tail
        elif word[0] in self.nexts:
            self.nexts[word[0]].insert(word[1:])
        # char not in dict, so make subtrie and descend
        else:
            self.nexts[word[0]] = Trie()
            self.nexts[word[0]].insert(word[1:])

if __name__ == "__main__":
    zog = Trie()
    to_insert = [
        #"hi",
        "ho",
        "hill",
        #"ahab",
        #"ahab",
        #"ahb",
    ]
    for key in to_insert:
        zog.insert(key)
    #zog.pprint()
    print zog.as_string()
