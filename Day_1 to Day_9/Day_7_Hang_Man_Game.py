import random
import hangman_words
import hangman_art
print(hangman_art.logo)
stages = hangman_art.stages
blank=[]
end_game=False
lives=6
word=random.choice(hangman_words.word_list)
for i in range(len(word)):
    blank+="_"
print(f"{' '.join(blank)}\n")
word=list(word)
while not end_game:
    guess=input("Guess the letter : ").lower()
    for i in range(len(word)):
        if word[i]==guess:
            blank[i]=guess
            if guess in blank:
                print(f"You've already guessed {guess}")
    if guess not in word:
        lives-=1
        print(f"You guessed {guess} , that's not in the word. You Lose a Life.")
        print(stages[lives])
        if lives==0:
            print(stages[0])
            print("You Lose!")
            end_game=True
    print(f"{' '.join(blank)}")
    if "_" not in blank:
            print("You Win!")
            end_game=True
    
