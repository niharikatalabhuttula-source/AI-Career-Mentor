def extract_skills(text):
    """
    Extracts skills from the resume text.
    Returns a list of detected skills.
    """

    # List of skills to search for
    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",
        "Power BI",
        "Tableau",
        "Excel",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "C",
        "C++",
        "C#",
        "React",
        "Node.js",
        "Django",
        "Flask",
        "TensorFlow",
        "PyTorch",
        "NumPy",
        "Pandas",
        "Scikit-learn"
    ]

    detected_skills = []

    # Convert resume text to lowercase
    text = text.lower()

    # Check each skill
    for skill in skills:
        if skill.lower() in text:
            detected_skills.append(skill)

    return detected_skills