Everyone knows that practice makes perfect, but the secret is that practice has to be focused and challenging to actually matter. Part of the difficulty with practicing creative activities like art, music or programming is choosing assignments to consistently challenge yourself without falling into a rut. StoryDice+ solves this problem by generating a prompt for you to work on every time you use it. It is highly extensible; it works by reading an XML file you supply.

# XML Specification

Name: `ideas.xml` by default, or whatever you tell the script to generate

`<idea>` tags are the basic building block. Every element of `ideas.xml` must be an `idea`. `idea`s can have arbitrarily many children. When the python script generates the task for the day, it selects an `idea` based on given weights and then does the same for the `idea`'s children. `idea`s must have the following attributes:

* `type` - This must be one of two values: "sequence" or "select". Depending on which is given, the behavior varies widely:
	* "sequence" - Every `idea` of this type will be evaluated in depth-first order and then shown to the user. Siblings of `type` "sequence" will be shown sequentially in the order they appear in `ideas.xml`.
	* "select" - At every node with one or more "select" `idea`s, the script will choose **only one** of them based on their `weight`s (see below), evaluate the chosen `idea` and its children, and then display that to the user. If a node has both "select" and "sequence" `idea`s, the chosen "select" `idea` will be shown sequentially based on the position of the first "select" `idea` in the document.

* `name` - Used to represent this value in the python script. This must be unique.

* `userstring` - The string that will be printed if this `idea` is selected. This does not need to be unique.
	* maybe add feature to allow userstring to be split in two before inserting next userstring

* `weight` - Random weight associated with this `idea` if it has `type` "select". This does not have to be normalized with respect to siblings — ie, if an `idea` has `weight` 3 and its only sibling has `weight` 2, it will be chosen 3/5 of the time while the sibling will be chosen 2/5 of the time.

* `dictionary` - A filename in the same directory of the script (or with the directory structure included) that lists a large amount of possible values. This attribute is optional, but if it's present, any child `idea`s will be ignored, and so will any `userstring`. If a `dictionary` attribute exists, the script will choose one value from the dictionary, with each equally weighted, and show the chosen value to the user as if it was the `userstring`.
