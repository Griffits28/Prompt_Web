import streamlit as st

# Configure the Streamlit page
st.set_page_config(page_title="ChatGPT Prompt Generator", layout="centered")
st.title("ChatGPT Prompt Generator")

# Step 1: Scenario selection
st.markdown("**Step 1: Select your target scenario (enter a number and press Enter)**")
scene = st.number_input(
    label="", 
    min_value=1, max_value=4, value=1, step=1,
    format="%d",
    help="1=Write cover letter; 2=Summarize article; 3=Generate code; 4=Translate document"
)

# Step 2: Dynamically display input fields based on scenario
st.markdown("**Step 2: Fill in the required information**")
if scene == 1:
    # Inputs for cover letter scenario
    job_title = st.text_input("Target Position:")
    company = st.text_input("Company Name:")
    skills = st.text_input("Skills/Experience to Highlight:")
    tone = st.text_input("Tone (e.g., formal, persuasive):")
elif scene == 2:
    # Inputs for article summary scenario
    topic = st.text_input("Article Topic:")
    focus = st.text_input("Key Points to Emphasize (e.g., conclusions):")
    length = st.text_input("Desired Summary Length (e.g., 100 words):")
elif scene == 3:
    # Inputs for code generation scenario
    task = st.text_input("Task Description:")
    language = st.text_input("Programming Language:")
    constraints = st.text_input("Additional Constraints (optional):")
elif scene == 4:
    # Inputs for translation scenario
    target_lang = st.text_input("Target Language (e.g., French):")
    usage = st.text_input("Usage Context (e.g., travel):")
    tone2 = st.text_input("Tone (e.g., natural, formal):")

# Step 3: Generate and display the final prompt
if st.button("Generate Prompt"):
    if scene == 1:
        # Construct prompt for cover letter
        prompt = (
            f"Please help me write a cover letter for the position of {job_title} at {company}. "
            f"Highlight my skills and experience in {skills}, and use a {tone} tone."
        )
    elif scene == 2:
        # Construct prompt for article summary
        prompt = (
            f"Please summarize an article on '{topic}', emphasizing {focus}, "
            f"and keep the summary within {length}."
        )
    elif scene == 3:
        # Construct prompt for code generation
        extra = f"{constraints} " if constraints else ""
        prompt = (
            f"Please write a program in {language} that accomplishes the following task: {task}. "
            f"{extra}Include comments and explanations for key sections."
        )
    else:
        # Construct prompt for translation
        prompt = (
            f"Please translate the following text into {target_lang} with a {tone2} tone, "
            f"suitable for {usage} context: <insert text here>"
        )

    # Display the generated prompt
    st.markdown("**Generated ChatGPT Prompt:**")
    st.code(prompt, language="text")