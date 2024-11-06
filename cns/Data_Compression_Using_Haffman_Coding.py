import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for the heap
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the tree

def build_codes(node, current_code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)
    return codes

def huffman_coding(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    return codes

def compress(text):
    codes = huffman_coding(text)
    compressed_text = ''.join(codes[char] for char in text)
    return compressed_text, codes

def decompress(compressed_text, codes):
    # Reverse the codes dictionary to decode
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

# Example usage
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    print("Original text:", text)

    compressed_text, codes = compress(text)
    print("Compressed text:", compressed_text)
    print("Huffman Codes:", codes)

    decoded_text = decompress(compressed_text, codes)
    print("Decoded text:", decoded_text)
