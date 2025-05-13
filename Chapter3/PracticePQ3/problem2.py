# Write a program  to fill in aletter template given bleow with name and date
# letter = '''
# Dear <|Name|>,
# you are selected!
# <|date|>
# ... 


letter = ''' Dear <|Name|>,
          you are selected!
         <|Date|> '''
print(letter.replace("<|Name|>", "Alisha").replace("<|Date|>", "2025"))




