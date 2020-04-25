## caesar
Simple program to encode or bruteforce using GPU text's encrypted with caesar cipher

# Getting started:
arguments:
  -t,--text - type or paste some text to encode/decode
  -s,--stride - enter the stride if you're encoding text with your key or leave empty if you're decoding ciphertext with unknown key
  -h, --help - displays help with familiar message
# Used modules
* cupy - working with vectors/matrix/tensors. CuPy is using cuda and storing data on GPU that decreases time to run this scrpit
* argparse - adding ability to work with arguments that were given in terminal
