import random
def generate_password(length=6):
  """Generate a random password of the specified length.

  Args:
    length: The length of the password to generate.

  Returns:
    A string containing the generated password.
  """

  # Create a list of all possible characters that can be used in a password.
  characters = [
      'abcdefghijklmnopqrstuvwxyz',
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      '0123456789',
      '!@#$%^&*()-_=+{}[]:;"<>,.?'
  ]

  # Generate a random password by randomly selecting characters from the list.
  password = ''
  for i in range(length):
    password += random.choice(characters)

  # Return the generated password.
  return password

password=generate_password()
print(password)