import streamlit as st

# Function to calculate points based on answers
def calculate_points(answers):
    points = 0
    for answer in answers:
        if answer == "Yes":
            points += 2
        elif answer == "Somewhat":
            points += 1
    return points

# Main Streamlit app
def main():
    st.title("3D Printer Selection Test")

    st.write("Welcome to the 'Would You Actually Need This Specific 3D Printer' Test! "
             "Before you invest in a 3D printer, answer the following questions to determine if it's the right fit for your needs:")

    # Questions and Answers
    questions = [
        "Are you planning to use the 3D printer for personal projects, hobbies, or professional applications?",
        "Do you have a specific budget in mind for the 3D printer and its associated accessories (filaments, maintenance, etc.)?",
        # ... (Add all questions here)
        "Are there specific environmental factors (ventilation, temperature) you need to consider for the 3D printer in your chosen location?"
    ]

    answers = []

    for question in questions:
        response = st.radio(question, ["Yes", "Somewhat", "No"])
        answers.append(response)

    # Calculate points
    points = calculate_points(answers)

    # Display results
    st.write("\n\nNow, add up your points based on your answers:")
    st.write(f"Total Points: {points}")

    # Interpretation
    if points >= 15:
        st.write("High likelihood that this 3D printer meets your needs.")
    elif 10 <= points <= 14:
        st.write("Consider if the printer's strengths align with your priorities.")
    else:
        st.write("Reevaluate your choice or explore other 3D printer options based on your requirements.")

if __name__ == "__main__":
    main()
