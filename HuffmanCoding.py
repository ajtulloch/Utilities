from collections import defaultdict
from heapq import heapify, heappop, heappush
import json

#------------------------------------------------------------------------------

class Node(object):
   def __init__(self, value, weight = 0, left = None, right = None):
       self.value = value
       self.weight = weight
       self.left = left
       self.right = right

   def __cmp__(self, other):
       return cmp(self.weight, other.weight)

   def is_leaf(self):
       return self.left == None and self.right == None

#------------------------------------------------------------------------------

class HuffmanCoding(object):
    def __init__(self, input_string):
        self.input_string = input_string
        self.encoding = []
    
    def _count_input(self):
        # Returns a list of (char, count) pairs, representing the count of each
        # character in the input string 
        count_dict = defaultdict(int)
        for char in self.input_string:
            count_dict[char] += 1
        l = [(k, v) for k, v in count_dict.iteritems()]
        return l
        
    @staticmethod
    def _compute_huffman_encoding(input_list):
        l = [Node(k, v) for k, v in input_list]
        heapify(l)

        while len(l) > 1:
            n1, n2 = heappop(l), heappop(l)
            n = Node(None, n1.weight + n2.weight, n1, n2)
            heappush(l, n)

        return l[0]
    
    def _compute_huffman_code(self, node, code = ""):

        if node is None:
            return
        else:
            node.code = code
            # Add values to encoding
            self._compute_huffman_code(node.left, code + "0")
            if node.value is not None:
                self.encoding.append((node.code, node.value))
            self._compute_huffman_code(node.right, code + "1")
            
            
    def _print_encoding(self):
        if self.encoding == []:
            raise ValueError("Encoding is empty!")
        for k, v in sorted(self.encoding, key = lambda x: len(x[0])):
            print "{0}\t{1}".format(k, v)
    
    def _encode(self):
        keys = self.encoding.keys()
        
    def huffman_encoding(self):
        l = self._count_input()
        n = self._compute_huffman_encoding(l)
        encoding = self._compute_huffman_code(n)
        self._print_encoding()
        
    @staticmethod
    def encoding(l, type):
        """Returns an output representing the encoding.
        Output is a dictionary of key, value pairs with key 
        being the encoded value and value being the original value."""
        d = {}
        for k, v in l:
            d[k] = v
            
        if type == "JSON":
            return json.dumps(d)
        if type == "Python":
            return d
        
    def decoding():
        pass
#------------------------------------------------------------------------------






input = "appppppppplebeespppp"

h = HuffmanCoding(input)
h.huffman_encoding()
# 
# output = huffman_encoding(count_input(input))
# arr = []
# huffman_code(output, "", arr)
# print sorted(arr)   
# 
