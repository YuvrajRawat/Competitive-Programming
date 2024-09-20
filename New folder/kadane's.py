def reverse_string_with_digit_count(input_string):

  
  # Split the input string into a list of words.
  words = input_string.split()

  # Reverse the order of the words in the list.
  words.reverse()

  # Add the number of digits in the first word of the input string to the
  # beginning of the first word of the output string.
  first_word = words[0]
  digit_count = len([c for c in first_word if c.isdigit()])
  first_word = str(digit_count) + first_word
  words[0] = first_word

  # Join the words in the list back into a string.
  output_string = " ".join(words)

  return output_string


# Example usage:
input_string = "My name is Yuvraj"
output_string = reverse_string_with_digit_count(input_string)
print(output_string)
