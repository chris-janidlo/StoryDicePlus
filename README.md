Everyone knows that practice makes perfect, but the secret is that practice has to be focused and challenging to actually matter. Part of the difficulty with practicing creative activities like art, music or programming is choosing assignments to consistently challenge yourself without falling into a rut. StoryDice+ solves this problem by generating a prompt for you to work on every time you use it. It is highly extensible; it works by reading an XML file you supply.

# XML Specification

Name: `ideas.xml` by default

Root element: `<idea>`

Tags: The tag of each element other than the root must be one of two values: `sequence` or `select`. Depending on which is given, the behavior varies as following:
	* `<sequence>` - Every element with this tag will be evaluated in depth-first order and then shown to the user as specified below. Siblings will be shown sequentially in the top-to-bottom order they appear the XML file.
	* `<select>` - At every node with one or more `<select>`s, the script will choose **only one** of them based on their `weight`s (see below), evaluate the chosen `<select>` and its children, and then display that to the user. If a node has both `<select>`s and `<sequence>`s, the chosen `<select>` will be shown sequentially with respect to the `<sequence>`s based on the position of the first `<select>` in the node.

`<select>`s must have the following attribute:

* `weight` - Random weight. This does not have to be normalized with respect to siblings — ie, if a `<select>` has `weight` 3 and its only sibling has `weight` 2, it will be chosen 3/5 of the time while the sibling will be chosen 2/5 of the time.

Each element may have the following attributes:

* `output` - The final output of the program is made by concatenating the value of `output` at each node in the order in which it is visited. Since evaluation is depth-first, the `output`s of any child elements will be seen before those of any siblings. Even though the order is depth-first, parents will be shown before children, because the program will necessarily visit the parents first. Between mutliple `<select>` elements under one parent, the end output will only use one of their `output`s. If this value is absent in a node, the script will treat the node as if `output` were set to "" (the empty string).
	* maybe add feature to allow output to be split in two before inserting next output

* `dictionary` - A filename in the same directory of the script (or with the directory structure included) that lists a large amount of possible values. If a `dictionary` attribute exists, the script will choose one value from the dictionary, with each equally weighted, and show the chosen value to the user as if it was the `output`. If this attribute is present, any `output` attribute will be ignored.

* `range-low` and `range-high` - Two integer values that denote the limit of a random range choice. If both are present, the output of this element will be a random number within that range.

* `name` - Used to uniquely represent this element. Currently unused by the script.

In the case that multuiple optional attributes are present, the script generates output based on the following hierarchy:

`range > dictionary > output`