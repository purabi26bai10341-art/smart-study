
# this system helps in ebtter management of studies 
# a computer science project helpful for students

subjects = {
    "Python": [
        "Variables",
        "Data Types",
        "Operators",
        "If-Else",
        "Loops",
        "Lists",
        "Functions"
    ],

    "Mathematics": [
        "Limits",
        "Continuity",
        "Differentiation",
        "Integration",
        "Differential Equations"
    ],

    "Physics": [
        "Mechanics",
        "Waves",
        "Electricity",
        "Optics"
    ],

    "English": [
        "Communication",
        "Listening",
        "obstacle",
        "Verbal Communication",
        "Non-Verbal Communication"
    ]
}


# this function keeps your performance which will help students to retrieve it
performance = {}

# it is string details of quiz which will help in better analysis of students knowledge
total_quizzes = 0
total_questions = 0
correct_answers = 0


# -------------------------------------------------
# showing the menu so thst students can see the details of their system
# -------------------------------------------------

def display_menu():

    print("\n" + "=" * 45)

    print("              SMARTSTUDY")
    print("       Personalized Study Assistant")

    print("=" * 45)

    print("1. View Subjects & Topics")

    print("2. Take a Quiz")
    print("3. Analyze My Performance")
    print("4. Find My Weak Topics")
    print("5. Get Study Recommendations")

    print("6. Create a Study Plan")
    print("7. View Progress")
    print("8. Exit")

    print("=" * 45)


# -------------------------------------------------
# showing subjetcs
# -------------------------------------------------

def view_subjects():

    print("\n========== SUBJECTS & TOPICS ==========")

    for subject in subjects:

        print("\n" + subject)

        topics = subjects[subject]

        for i in range(len(topics)):
            print("  ", i + 1, ".", topics[i])


# -------------------------------------------------
# students must answer these questions to know their level in each subject
# -------------------------------------------------

quiz_questions = {

    "Python": [
        {
            "topic": "Variables",
            "question": "Which symbol is used to assign a value to a variable?",
            "options": ["==", "=", "!=", ":"],
            "answer": 2
        },

        {
            "topic": "Data Types",
            "question": "Which data type is used for whole numbers?",
            "options": ["float", "string", "int", "list"],
            "answer": 3
        },

        {
            "topic": "Loops",
            "question": "Which loop is commonly used to traverse a list?",
            "options": ["for", "if", "def", "print"],
            "answer": 1
        },

        {
            "topic": "Functions",
            "question": "Which keyword is used to create a function?",
            "options": ["function", "define", "def", "fun"],
            "answer": 3
        }
    ],

    "Mathematics": [
        {
            "topic": "Limits",
            "question": "A limit tells us the value that a function approaches when:",
            "options": [
                "x approaches a value",
                "x becomes zero only",
                "function becomes constant",
                "none of these"
            ],
            "answer": 1
        },

        {
            "topic": "Differentiation",
            "question": "What is the derivative of x²?",
            "options": ["x", "2x", "x²", "2"],
            "answer": 2
        },

        {
            "topic": "Integration",
            "question": "What is the integral of 2x?",
            "options": [
                "x² + C",
                "2x² + C",
                "x + C",
                "2 + C"
            ],
            "answer": 1
        }
    ],

    "Physics": [
        {
            "topic": "Mechanics",
            "question": "What is the SI unit of force?",
            "options": [
                "Joule",
                "Newton",
                "Watt",
                "Pascal"
            ],
            "answer": 2
        },

        {
            "topic": "Electricity",
            "question": "What is the SI unit of electric current?",
            "options": [
                "Volt",
                "Ampere",
                "Ohm",
                "Watt"
            ],
            "answer": 2
        },

        {
            "topic": "Waves",
            "question": "What is the SI unit of frequency?",
            "options": [
                "Newton",
                "Hertz",
                "Joule",
                "Volt"
            ],
            "answer": 2
        }
    ],

    "English": [
        {
            "topic": "Communication",
            "question": "Who sends the message in the communication process?",
            "options": [
                "Receiver",
                "Sender",
                "Listener",
                "Audience"
            ],
            "answer": 2
        },

        {
            "topic": "Listening",
            "question": "Listening mainly involves:",
            "options": [
                "Only hearing",
                "Understanding the message",
                "Ignoring the speaker",
                "Speaking"
            ],
            "answer": 2
        },

        {
            "topic": "Non-Verbal Communication",
            "question": "naming non-verbal communication?",
            "options": [
                "Email",
                "Speech",
                "Facial expression",
                "Essay"
            ],
            "answer": 3
        }
    ]
}


# -------------------------------------------------
# attempting quiz by students
# -------------------------------------------------

def take_quiz():

    global total_quizzes
    global total_questions
    global correct_answers

    print("\n========== TAKE A QUIZ ==========")

    print("\nChoose a subject:")

    subject_list = list(quiz_questions.keys())


    for i in range(len(subject_list)):
        print(i + 1, ".", subject_list[i])

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError:
        print("Please enter a number.")
        return

    if choice < 1 or choice > len(subject_list):
        print("Invalid choice.")
        return

    selected_subject = subject_list[choice - 1]


    questions = quiz_questions[selected_subject]

    score = 0

    print("\nStarting", selected_subject, "quiz...")
    print("There are", len(questions), "questions.")

    for i in range(len(questions)):

        question = questions[i]

        print("\nQuestion", i + 1)

        print(question["question"])

        for j in range(len(question["options"])):
            print(
                j + 1,
                ".",
                question["options"][j]
            )

        try:
            answer = int(input("Your answer: "))

        except ValueError:
            print("Invalid answer. Question skipped.")
            continue

        topic = question["topic"]

        # Creating a topic specially for students if it is not existing only
        if topic not in performance:
            performance[topic] = {
                "attempted": 0,
                "correct": 0
            }

        performance[topic]["attempted"] += 1

        total_questions += 1

        if answer == question["answer"]:

            print("Correct!")

            score += 1
            correct_answers += 1

            performance[topic]["correct"] += 1

        else:

            print("Wrong!")

            correct_option = question["options"][
                question["answer"] - 1
            ]

            print("Correct answer:", correct_option)

    total_quizzes += 1

    percentage = (score / len(questions)) * 100


    print("\n========== QUIZ RESULT ==========")

    print("Subject:", selected_subject)
    print("Score:", score, "/", len(questions))
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Great job! Keep it up.")

    elif percentage >= 60:
        print("Good work. A little more practice will help.")

    else:
        print("You need more practice in this subject.")


# -------------------------------------------------
# this funcion helps students to analyse their performance
# -------------------------------------------------

def analyze_performance():

    print("\n========== PERFORMANCE ANALYSIS ==========")


    if total_questions == 0:

        print("No quiz has been attempted yet.")
        print("Take a quiz first.")

        return

    percentage = (
        correct_answers / total_questions
    ) * 100

    print("Total quizzes:", total_quizzes)
    print("Total questions:", total_questions)
    print("Correct answers:", correct_answers)
    print("Overall accuracy:", round(percentage, 2), "%")

    print("\nTopic-wise performance:")

    for topic in performance:

        attempted = performance[topic]["attempted"]
        correct = performance[topic]["correct"]

        topic_percentage = (
            correct / attempted
        ) * 100

        print(
            topic,
            ":",
            correct,
            "/",
            attempted,
            "(",
            round(topic_percentage, 2),
            "%)"
        )


# -------------------------------------------------
# showing weak topics
# -------------------------------------------------

def find_weak_topics():

    print("\n========== WEAK TOPICS ==========")


    if len(performance) == 0:

        print("No data available.")
        print("Take a quiz first.")

        return

    weak_found = False

    for topic in performance:

        attempted = performance[topic]["attempted"]

        correct = performance[topic]["correct"]

        percentage = (
            correct / attempted
        ) * 100

        if percentage < 60:

            print(
                "-",
                topic,
                ":",
                round(percentage, 2),
                "%"
            )

            weak_found = True

    if weak_found == False:

        print("No weak topics found!")

        print(
            "Your current performance is good."
        )


# -------------------------------------------------
# giving tips of study for betterment of students
# -------------------------------------------------

def study_recommendations():

    print("\n========== STUDY RECOMMENDATIONS ==========")

    if len(performance) == 0:

        print("Take a quiz first.")
        print(
            "Then SmartStudy will give "
            "personalized recommendations."
        )

        return

    weak_topics = []

    for topic in performance:

        attempted = performance[topic]["attempted"]
        correct = performance[topic]["correct"]

        percentage = (
            correct / attempted
        ) * 100

        if percentage < 60:
            weak_topics.append(topic)

    if len(weak_topics) == 0:

        print("You are doing well!")

        print(
            "Keep revising your topics and "
            "continue taking quizzes."
        )

        return

    print("Based on your quiz performance:")



    for topic in weak_topics:

        print("\nTopic:", topic)

        print("Recommendation:")
        print("- Revise the basic concepts.")
        print("- Make short notes.")
        print("- Solve practice questions.")
        print("- Take the quiz again.")


# ---------------------------------------------
# create effective study plan which is helpful for students
# -------------------------------------------------

def create_study_plan():

    print("\n========== CREATE STUDY PLAN ==========")


    try:

        days = int(
            input("Enter number of days: ")
        )

        hours = float(
            input("How many hours can you study per day? ")
        )

    except ValueError:

        print("Please enter valid numbers.")
        return

    if days <= 0 or hours <= 0:

        print("Days and hours must be greater than zero.")
        return

    print("\n========== YOUR STUDY PLAN ==========")

    subject_list = list(subjects.keys())

    for day in range(1, days + 1):

        subject = subject_list[
            (day - 1) % len(subject_list)
        ]

        topic_list = subjects[subject]

        topic = topic_list[
            (day - 1) % len(topic_list)
        ]

        print("\nDay", day)
        print("-------------------------")
        print("Subject:", subject)
        print("Topic:", topic)
        print("Study time:", hours, "hours")

        print("Suggested routine:")
        print("- Concept study")
        print("- Practice questions")
        print("- Quick revision")


# -------------------------------------------------
# tracks the progress of students to let them know where they stand
# -------------------------------------------------

def view_progress():

    print("\n========== MY PROGRESS ==========")

    if total_questions == 0:

        print("No progress available yet.")
        print("Take your first quiz!")

        return

    percentage = (
        correct_answers / total_questions
    ) * 100

    print("Quizzes taken:", total_quizzes)
    print("Questions attempted:", total_questions)
    print("Correct answers:", correct_answers)
    print("Overall accuracy:", round(percentage, 2), "%")

    print("\nProgress:")

    if percentage >= 80:

        print("[##########] Excellent")

    elif percentage >= 60:

        print("[#######---] Good")

    elif percentage >= 40:

        print("[#####-----] Average")

    else:

        print("[###-------] Needs Improvement")


# -------------------------------------------------
# this is the function which will call the main function and execute the code successfully
# -------------------------------------------------

def main():

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            view_subjects()

        elif choice == "2":

            take_quiz()

        elif choice == "3":

            analyze_performance()

        elif choice == "4":

            find_weak_topics()

        elif choice == "5":

            study_recommendations()

        elif choice == "6":

            create_study_plan()

        elif choice == "7":

            view_progress()

        elif choice == "8":

            print(
                "\nThank you for using SmartStudy!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please enter a number from 1 to 8."
            )


# -------------------------------------------------
# letsssss gooo
# -------------------------------------------------

if __name__ == "__main__":

    main()