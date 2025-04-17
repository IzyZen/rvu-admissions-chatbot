# chatbot_logic.py
import openai

# Replace with your own OpenAI API key
openai.ak = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you got it
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def start_chat():
    print("Hey Wassup! Welcome to the RVU Chatbot :)")
    print("Ask me your questions but first,\n")
    print("Are you an already existing student in RVU?")
    print("1. Yes\n2. No")
    choice = input("Enter 1 or 2: ")

    if choice.strip() == "2":
        print("\nOkay then, Welcome to RV University!\n")
        tour_menu()
    else:
        i = int(input("Okay RVU Student! What is your USN? (Last 3 digits): "))


def tour_menu():
    print("How may I be of service?")
    print("1. I want to Join RVU\n2. I'm just looking around")
    input("Enter 1 or 2: ")  # Both go to same response
    print("Great, allow me to show you around then!")

    while True:
        print("\nTour Menu:")
        print("1. Courses & Degrees Offered")
        print("2. Fee Structure")
        print("3. Code of Conduct")
        print("4. Show me some Images")
        print("5. RVU & History of Origin")
        print("6. Location")
        print("7. Contact Live Agent")
        print("8. Others (AI Chat)")
        print("9. Exit")
        
        selection = input("Choose an option (1-9): ").strip()
        
        if selection == "1":
            print("We offer a wide range of about 35 Courses to choose from in RV University! Everything from Engineering to Psychology, you name it!\nCheck it out:\nhttps://rvu.edu.in/undergraduate-courses-ug/")
        elif selection == "2":
            print("Here you go!\nhttps://rb.gy/l9yrqc")
        elif selection == "3":
            print("Here's the RVU Code of Conduct. Following rules and regulations is a must if you don't wanna get kicked out, haha I'm joking. (I'm not)\nhttps://rb.gy/32ques")
        elif selection == "4":
            print("Go here: https://rb.gy/b7vbz5")
        elif selection == "5":
            print("Great Choice!\nhttps://en.wikipedia.org/wiki/RV_University")
        elif selection == "6":
            print("Here we are! -> https://www.google.com/maps/search/?api=1&query=12.923,77.498")
        elif selection == "7":
            print("Contact Us at\nEmail: rvuadmissions@rvu.edu.in\nPhone: 88888 12128, 77872 41962")
        elif selection == "8":
            prompt = input("I am a recreated representation of Chatgpt 4.0 connected in the backend at botpress! I can give an answer to "What is the avg placement salary at RVU?" wanna hear it?[1/0]")
            if prompt == 1:
                print("Popular question! The earliest RVU batch hasn't yet graduated so there isn't an exact value I can give you, please do not fall for falsified information online. However, the companies that come to hire from RVCE, also come to RVU!.")


        elif selection == "9":
            print("Thanks for chatting! Have a great day :)")
            break
        else:
            print("Invalid input. Try again.")
            
start_chat()
