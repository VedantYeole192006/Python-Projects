# Terminal / GUI (optional)
# File I/O, dictionaries, tkinter GUI
# A CLI or GUI app to display flashcards. It should show a term, wait for input (e.g., "flip"), then show the definition.
# In progress
class Flash_card:
    def add_card():
        add = input("Add Question: ")
        ans = input("Write answer for the question: ")
        with open('Intermediate Project/Flashcardapp/flashque.txt', 'a') as file:
            file.writelines(add)
        with open('Intermediate Project/Flashcardapp/flashans.txt', 'a') as file2:
            file2.writelines(ans)
        
    def rem_card():

        with open('Intermediate Project/Flashcardapp/flashque.txt', 'r') as file:
            a = file.readlines()
            ptr = 1

        rem = int(input("Which line number do you want to remove? "))

        with open('Intermediate Project/Flashcardapp/flashque.txt', 'w') as file:    
            for line in a:
                if ptr != rem:
                    file.write(line)
                ptr += 1

            print(a)

        with open('Intermediate Project/Flashcardapp/flashans.txt', 'r') as file2:
            b = file2.readlines()
            ptr2 = 1
        
        with open('Intermediate Project/Flashcardapp/flashans.txt', 'w') as file2:
            for line in b:
                if ptr2 != rem:
                    file.write(line)
                ptr2 += 1

        print("Deleted...")

    # def review_card():
    #     with open('Intermediate Project/Flashcardapp/flashque.txt', 'r') as fr:
    #         read = fr.readlines()
    #         count = 1
    #         for line in read:


inp = input("What task do you want to perform? ")

if inp.lower() == "add":
    Flash_card.add_card()

elif inp.lower() == "remove":
    Flash_card.rem_card()
    