#!/usr/bin/env python3

class MyString:
  def __init__(self, val= ''):
    if not isinstance(val, str):
      raise ValueError('The value must be a string.')
    self.val = val
    
  def is_sentence(self):
    return self.val.endswith('.')

  def is_question(self):
    return self.val.endswith('?')

  def is_exclamation(self):
    return self.val.endswith('!')
  
  def count_sentences(self):
    mod_val = self.val.replace('.', ' ').replace('?', ' ').replace('!', ' ') # replace all punctuation marks with a space
    sentences = mod_val.split() # split into sentences based on spaces
    return len(sentences)


