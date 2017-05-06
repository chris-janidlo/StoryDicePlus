import xml.etree.ElementTree as ET
import random

SELECT = 'select'
SEQUENCE = 'sequence'
WEIGHT = 'weight'
RANGE_LOW = 'range-low'
RANGE_HIGH = 'range-high'
DICTIONARY = 'dictionary'
OUTPUT = 'output'

def gather_selects (element):
	grab_bag = list()
	for child in element:
		if child.tag == SELECT:
			grab_bag.extend([child] * int(child.attrib[WEIGHT]))
	return random.choice(grab_bag)

#given an element, return the output value, whether that is the actual output string or a range value or a dictionary value
def get_output (element):
	attr = element.attrib
	if RANGE_LOW in attr or RANGE_HIGH in attr:
		rand_num = random.randint(int(attr[RANGE_LOW]), int(attr[RANGE_HIGH]))
		return str(rand_num)
	if DICTIONARY in attr:
		with open(attr[DICTIONARY], 'r') as f:
			grab_bag = f.readlines()
		return (random.choice(grab_bag)).rstrip()
	if OUTPUT not in attr:
		return ''
	return attr[OUTPUT]

def traverse_tree (root):
	selected = False
	element = None
	output = get_output(root)
	for child in root:
		if child.tag == SELECT:
			if selected: 
				continue	
			element = gather_selects(root)
			selected = True
		else:
			element = child
		output += traverse_tree(element)
	return output

def main ():
	tree = ET.parse('ideas.xml')
	root = tree.getroot()
	print(traverse_tree(root))

main()