from pprint import pprint
from collections import defaultdict
import heapq as hq
# Based on https://rosettacode.org/wiki/Huffman_coding#Python 
# Compress an input text ussing Huffman Coding

inText = 'this is an example for huffman encoding'

class Node:
	weight = None
	frequency = 0
	
	def __init__(self, w, f):
		self.weight = w
		self.frequency = f
		
	# represents the object for pprinting it
	def __repr__(self):
		return "<value: '%s', frequency: '%s'>" % (self.value, self.frequency)


# Returns a dictionary of frequencies accesible by a character on string
def getFrequencies(string):
	frequencies = defaultdict(int)
	for c in string:
		# we count negatively to enforce a max-heap instead of a min-heap
		frequencies[c] += 1
	return frequencies

def huffman(freq):
	heap = [[wt, [sym, ""]] for sym, wt in frequencies.items()]
	hq.heapify(heap)
	while len(heap) > 1:
		lo = hq.heappop(heap)
		hi = hq.heappop(heap)
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		hq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	return sorted(hq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

#	
# Main
#

frequencies = getFrequencies(inText)
huff = huffman(frequencies)
pprint(huff)



	
