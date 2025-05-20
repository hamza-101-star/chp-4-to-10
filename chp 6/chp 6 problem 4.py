glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that only runs when it is called.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable sequence of values.',
    'boolean': 'A data type that can be either True or False.',
    'if statement': 'A control structure that lets you execute code based on a condition.',
    'string': 'A sequence of characters used to represent text.',
    'comment': 'A note in the code that is not executed, used to explain what the code does.'
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")
