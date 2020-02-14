import time
import sys
import random 

def fortune(fortune):
    if fortune == 1:
        return "Yes"
    elif fortune == 2:
        return "No"
    elif fortune == 3:
        return "Doesn't look likely"
    elif fortune == 4:
        return "It could happen"
    elif fortune == 5:
        return "Perhaps"
    elif fortune == 6:
        return "Definitely not"

print("""
                    ____ 
                  .'* *.'
               __/_*_*(_
              / _______ 
             _\_)/___\(_/_ 
            / _((\- -/))_ 
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' 
           / _ \ - | - /_  
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ 
             / .   .   . 
            /   .     .   
           /   /   |   \   
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(________mrf\____.dBBBb.________)____)
""")
print("")
question = input("What would you like to ask?\nQuestion: ")
print("")
print("The crystal ball starts to glow...")
time.sleep(2)
print("")
print("The walls start to shake surrounding you...")
time.sleep(2)
fortune = fortune(random.randint(1,6))
print("")
print("Words start to appear in the crystal ball...")
print("")
print(f"""
         _...._
       .`      `.
      / ***      \         The Crystal Ball
     : **         :         says.........
     :            :            {fortune}
      \          /       
       `-.,,,,.-'             
        _(    )_
       )        (
      (          )
       `-......-`
""")


