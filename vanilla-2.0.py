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
            max_tokens=500,
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
    grade = st.text_input('Grade', "8th")
    subject = st.text_input('Subject', "History")
    topic = st.text_input('Topic', "Great Depression")
    learning_objectives = st.text_area('Learning Objectives', "Students will examine how the economic practices of the 1920s contributed to the coming of the Great Depression.")

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
        1. Authentic Problems: Develop real-world problems or scenarios relevant to students’ personal lives or communities. Ensure these problems are meaningful and relatable, drawing on their lived experiences.
        2. Goal-Directed Learning: Encourage students to set clear, personalized goals related to the learning objectives. Incorporate strategies for students to reflect on their goals and plan the steps needed to achieve them.
        3. Making Choices: Provide students with options in how they engage with the content, such as choosing learning activities, tools, or even the physical or virtual spaces where they work. Highlight opportunities for decision-making throughout the lesson.
        4. Taking Actions: Design activities that require students to take initiative and act on their ideas. Include opportunities for students to identify problems and take proactive steps to address or respond to them.
        5. Problem-Solving: Promote independence and critical thinking by engaging students in problem-solving tasks where they explore solutions, articulate their reasoning, and support their peers in overcoming challenges.
        6. Self-Efficacy: Incorporate self-reflection exercises that allow students to assess their progress and strategies. Provide opportunities for students to build confidence in their abilities, including self-regulation and constructive self-assessment.
        7. Interaction: Design tasks that involve meaningful interaction with both their peers and their environment. This could include hands-on activities, discussions, or collaborative projects that make use of real-world materials or scenarios.
        8. Collaboration: Facilitate group activities where students collaborate through discussion, idea synthesis, and constructive feedback to solve problems and create shared outcomes.
        9. Opportunities to Share Ideas: Create spaces for students to share their ideas and ensure that every voice is heard. Plan for presentations, group discussions, or platforms where students’ insights can be acknowledged and discussed.
        10. Playing Different Roles: Empower students to take on various roles in the classroom, particularly in the assessment process. Encourage self and peer assessment where students critique and reflect on their own or others' work.
        11. Sharing Authority: Give students greater control over their learning by involving them in decisions about assessment methods, content topics, or how their learning environment is structured. Support co-construction of learning experiences to give them a sense of ownership.

        Please generate a detailed lesson plan including Grade, Subject, Topic, Opening, Introduction, Guided Practice, Independent Practice, Closing, Assessment, Extension Activity, and Homework.
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
