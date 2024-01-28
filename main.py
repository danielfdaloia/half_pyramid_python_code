def display_asterisk_triangle(rows):
  for i in range(1, rows + 1):
      for j in range(i):
          print('*', end='')
      print()

# Number of rows in the triangle
num_rows = 10

# Call the function to display the asterisk triangle
display_asterisk_triangle(num_rows)
