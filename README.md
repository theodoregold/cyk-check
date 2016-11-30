### What is this?
Small Python script for checking if a word is part of [CFG (Context-free Grammar)](http://en.wikipedia.org/wiki/Context-free_grammar) or not. This script is implementing [CYK (Cocke–Younger–Kasami) algorithm](http://en.wikipedia.org/wiki/CYK_algorithm). 

At the time, I couldn't find any simple/understandable implementation of CYK algorithm that I liked. If you have any questions feel free to create an issue.

Note: Your language must be in [Chomsky form](http://en.wikipedia.org/wiki/Chomsky_normal_form).

### Getting started
It's really straight forward. Change `productions` and `start_symbol` variables to your specific case. Then, just run it. Enter any word and see if it is part of the grammer.

### TO-DO
 * include grammer from seperate JSON file in runtime
 * convert any CFG to Chomsky form 
 * add some checks

### Issues
Found a bug or better solution? Please report to the issue section.
