
import random
List=["Hello","Race","Turtle","Pen","Uncle"]
max=6
selected_word=random.choice(List).lower()
secret_word=["_"]*len(selected_word)
print("Welcome to Hangman Game!")
while max>0:
    current_display="".join(secret_word)
    print(f"Current Status:{current_display}")
    if current_display!=selected_word:
     answer=input("Enter your answer:").lower()
     if answer in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i]==answer:
              if secret_word[i]=="_":    
               secret_word[i]=answer
              else:
                  max-=1
     else:
        max-=1
    else:
       print(f"Congratulations!The word was {selected_word}")
       print("You Win!")
       break           
else:
   print("Game Over")
   print(f"The word was {selected_word}")