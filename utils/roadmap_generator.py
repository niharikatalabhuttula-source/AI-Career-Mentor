def generate_roadmap(recommended_roles):
    """
    Generates a learning roadmap based on the recommended career roles.
    Returns a list of learning steps.
    """

    roadmap = []

    if "AI Engineer" in recommended_roles:
        roadmap.extend([
            "Week 1 → Python",
            "Week 2 → NumPy & Pandas",
            "Week 3 → Machine Learning",
            "Week 4 → Deep Learning",
            "Week 5 → TensorFlow",
            "Week 6 → Git & GitHub",
            "Week 7 → Docker",
            "Week 8 → AWS Basics"
        ])

    elif "Machine Learning Engineer" in recommended_roles:
        roadmap.extend([
            "Week 1 → Python",
            "Week 2 → NumPy & Pandas",
            "Week 3 → Machine Learning",
            "Week 4 → Scikit-learn",
            "Week 5 → TensorFlow",
            "Week 6 → Model Deployment"
        ])

    elif "Data Scientist" in recommended_roles:
        roadmap.extend([
            "Week 1 → Python",
            "Week 2 → Statistics",
            "Week 3 → Pandas & NumPy",
            "Week 4 → Data Visualization",
            "Week 5 → Machine Learning",
            "Week 6 → SQL"
        ])

    elif "Data Analyst" in recommended_roles:
        roadmap.extend([
            "Week 1 → Excel",
            "Week 2 → SQL",
            "Week 3 → Python",
            "Week 4 → Pandas",
            "Week 5 → Power BI",
            "Week 6 → Tableau"
        ])

    elif "Frontend Developer" in recommended_roles:
        roadmap.extend([
            "Week 1 → HTML",
            "Week 2 → CSS",
            "Week 3 → JavaScript",
            "Week 4 → React",
            "Week 5 → Git & GitHub"
        ])

    elif "Full Stack Developer" in recommended_roles:
        roadmap.extend([
            "Week 1 → HTML & CSS",
            "Week 2 → JavaScript",
            "Week 3 → React",
            "Week 4 → Node.js",
            "Week 5 → MongoDB",
            "Week 6 → Git & GitHub"
        ])

    elif "Python Developer" in recommended_roles:
        roadmap.extend([
            "Week 1 → Python Basics",
            "Week 2 → OOP",
            "Week 3 → File Handling",
            "Week 4 → APIs",
            "Week 5 → Flask/Django"
        ])

    elif "Java Developer" in recommended_roles:
        roadmap.extend([
            "Week 1 → Java Basics",
            "Week 2 → OOP",
            "Week 3 → Collections",
            "Week 4 → JDBC",
            "Week 5 → Spring Boot"
        ])

    else:
        roadmap.append("No roadmap available for the selected role.")

    return roadmap