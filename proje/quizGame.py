#--------------------
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        
        question_num=question_num+1
        guess=(input("Cevabınızı giriniz (A,B,C Veya D): ")).upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)

    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer== guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#--------------------
def display_score(correct_guesses,guesses):
    print("---------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score= int((correct_guesses/len(questions))*100)
    print("skorunuz: "+str(score)+"%")

#--------------------
def play_again():
    response= input("Tekrar oynamak istiyor musun? (Evet/Hayır): ")
    response= response.upper()

    if response=="EVET":
        return True
    else:
        return False

#--------------------

questions ={
    "Pythonu kim oluşturmuştur?":"D",
    "Python hangi yıl oluşturulmuştur?":"C",
    "Mr.Bean hangi dalda diziler çekmiştir?":"C",
    "kedilerin bıyıkları vardır":"A"
}

options=[
 ["A. Elon Musk","B. Enner Valencia","C. Volkan Demirel","D. Guido Van Russom"],
 ["A. 1988","B. 2005","C. 1991","D. 1999"],
 ["A. Korku","B. Bilim Kurgu","C. Komedi","D. Drama"],
 ["A. Doğru","B. Yanlış","C. Bazen","D. Kedi bıyığı da ne?"],  
]

new_game()

while play_again():
    new_game()

print ("Byeeee!")