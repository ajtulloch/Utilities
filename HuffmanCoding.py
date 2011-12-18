from collections import defaultdict
from heapq import heapify, heappop, heappush

#------------------------------------------------------------------------------

class Node(object):
   def __init__(self, value, weight = 0, left = None, right = None):
       self.value = value
       self.weight = weight
       self.left = left
       self.right = right

   def __cmp__(self, other):
       return cmp(self.weight, other.weight)

#------------------------------------------------------------------------------

def _count_input(input_string):
    # Returns a list of (char, count) pairs, representing the count of each
    # character in the input string 
    count_dict = defaultdict(int)
    for char in input_string:
        count_dict[char] += 1
    l = [(k, v) for k, v in count_dict.iteritems()]
    return l
    
def _construct_huffman_tree(input_list):
    l = [Node(k, v) for k, v in input_list]
    heapify(l)

    while len(l) > 1:
        n1, n2 = heappop(l), heappop(l)
        n = Node(None, n1.weight + n2.weight, n1, n2)
        heappush(l, n)

    return l[0]

def _compute_huffman_traversal(node, code = "", arr = []):
    if node is None:
        return
    else:
        node.code = code
        # Add values to encoding
        _compute_huffman_traversal(node.left, code + "0", arr)
        if node.value is not None:
            arr.append((node.code, node.value))
        _compute_huffman_traversal(node.right, code + "1", arr)


def _compute_huffman_dec_dict(input_string):
    l = _count_input(input_string)
    n = _construct_huffman_tree(l)
    enc_l = []
    _compute_huffman_traversal(n, "", enc_l)
    dec_d = dict(enc_l)
    return dec_d
        
def _compute_huffman_enc_dict(input_string, dec_d = None):
    if dec_d == None:
        dec_d = _compute_huffman_dec_dict(input_string)
    enc_d = {}
    for k, v in dec_d.iteritems():
        enc_d[v] = k
    return enc_d
    
    
def encode(input_string):
    """Encodes a given string, using Huffman encoding.
    Returns a binary string and the decoding dictionary"""
    d = _compute_huffman_dec_dict(input_string)
    e = _compute_huffman_enc_dict(input_string, d)
    
    output_list = (e[c] for c in input_string)
    return "".join(output_list), d
    
def decode(encoded_string, dec_d):
    output_string = ""
    b = ""
    for c in encoded_string:
        b += c
        if b in dec_d:
            output_string += dec_d[b]
            b = ""
    return output_string



