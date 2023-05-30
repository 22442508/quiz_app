import streamlit as st

def main():
    st.title("Quiz App")
    st.markdown("Test your knowledge!")

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome", "Madrid"],
            "correct_option": 0
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Jupiter", "Venus", "Saturn"],
            "correct_option": 0
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "correct_option": 2
        }
    ]

    total_questions = len(questions)
    score = 0

    for i, question in enumerate(questions, 1):
        st.subheader(f"Question {i}/{total_questions}:")
        st.write(question["question"])
        selected_option = st.radio("Select an option:", options=question["options"])
        
        if selected_option == question["options"][question["correct_option"]]:
            score += 1

    st.success(f"You scored {score}/{total_questions}!")

if __name__ == "__main__":
    main()
