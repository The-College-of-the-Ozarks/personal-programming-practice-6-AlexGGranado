# Programming 1: Personal Programming Practice 6

---

Write programs to tackle the following problems. Use the specified .py file (in **bold**) for each part (each file should be created automatically in your repository). You may discuss and collaborate with your peers, but you should submit your own code and fully understand all code you submit. If you work with others on one of the parts, cite your collaborators in a comment near the top of that file.

1. In **str_ends.py**, write a program which takes a string input and outputs the first character, middle character, and last character of the string. If the string has even length, output the "first" middle character. For example, "Hopkins" should output H, k, s; "Programs" should output P, g, s.
2. In **remove.py**, write a program which takes two inputs: a string, and a character; and outputs the string with every copy of the given character removed. For example, inputs of "banana" and "a" should output "bnn". *Hint: we can construct a string character-by-character similar to how we compute the sum inside a loop. Create a variable to hold the new string and store in that variable an empty string. Then as each character you want to include appears, concatenate it (using +=) to this variable.*

You may earn bonus on remove.py in one of the following two ways (not both, for obvious reasons).
  - Add validation to ensure the second input is a single character
  - Allow multiple characters for the second input, and remove every copy of every character which appears in the second input. So "banana", "ab" would output "nn".
