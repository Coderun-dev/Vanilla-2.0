import streamlit as st
import openai

# Access the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# OpenAI API Key
openai.api_key = api_key

# Function to generate lesson plan
def generate_lesson_plan(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error generating lesson plan: {str(e)}")
        return None

# Streamlit app
def main():
    st.title("Student Agency-Focused Lesson Plan Generator")

    # Input fields for teacher preferences
    grade = st.text_input('Grade', "8th Grade")
    subject = st.text_input('Subject', "Counseling and Guidance")
    topic = st.text_input('Topic', "Empathy")
    learning_objectives = st.text_area('Learning Objectives', "Identify ways to show empathy")

    if st.button('Generate Lesson Plan'):
        # Create prompt dynamically
        teacher_input = {
            "grade": grade,
            "subject": subject,
            "topic": topic,
            "learning_objectives": learning_objectives,
        }

        prompt_template = """
        You are a lesson plan generation assistant focused on promoting student agency. A teacher has provided the following details for a lesson:

        Grade: {grade}
        Subject: {subject}
        Topic: {topic}
        Learning Objectives: {learning_objectives}

        Please generate a detailed lesson plan that emphasizes student agency, incorporating the following elements:
        1. **Authentic Problems**: Design real-world problems that connect to students' personal lives and are familiar to them.
        2. **Goal-Directed Learning**: Encourage students to actively think about their goals and outline strategic steps they can take to achieve these outcomes.
        3. **Competence Beliefs**: Include activities that help students build confidence in their abilities through self-reflection and self-regulation.
        4. **Choice and Autonomy**: Provide opportunities for students to choose topics, learning activities, or environments (e.g., virtual, physical, or outdoor spaces).
        5. **Action and Problem-Solving**: Design tasks where students act as problem-solvers, taking responsibility for their learning and helping peers.
        6. **Collaboration and Interaction**: Facilitate student collaboration, where they engage in discussions, critical thinking, and theorizing with peers to solve problems.
        7. **Opportunities to Share Ideas**: Create avenues for students to share and discuss their ideas with the class, ensuring their voices are heard.
        8. **Play Different Roles**: Empower students to assess their work or their peers' work, shifting the focus beyond responding to teacher-directed tasks.
        9. **Shared Authority**: Allow students to co-construct the curriculum and decide on forms of assessment, giving them greater control over their learning environment.

        Structure your response to include:
        - **Grade, Subject, Topic**
        - **Opening and Introduction**
        - **Guided Practice**: Activities that promote exploration and problem-solving
        - **Independent Practice**: Tasks that allow for student choice and reflection
        - **Collaboration Opportunities**
        - **Assessment and Reflection**: Strategies that involve self-assessment or peer assessment
        - **Extension Activity and Homework**: Meaningful and relevant tasks that support continued learning and self-efficacy
        """

        prompt = prompt_template.format(
            grade=teacher_input["grade"],
            subject=teacher_input["subject"],
            topic=teacher_input["topic"],
            learning_objectives=teacher_input["learning_objectives"],
        )

        # Generate and display the lesson plan
        lesson_plan = generate_lesson_plan(prompt)
        st.write(lesson_plan)

if __name__ == "__main__":
    main()
