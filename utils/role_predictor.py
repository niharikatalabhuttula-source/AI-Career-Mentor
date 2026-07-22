def predict_roles(skills):
    """
    Predicts suitable career roles based on detected skills.
    Returns a list of recommended roles.
    """

    roles = []

    skills = [skill.lower() for skill in skills]

    # AI / ML
    if "python" in skills and (
        "machine learning" in skills
        or "deep learning" in skills
        or "tensorflow" in skills
        or "pytorch" in skills
    ):
        roles.append("AI Engineer")
        roles.append("Machine Learning Engineer")
        roles.append("Data Scientist")

    # Data Analyst
    if "python" in skills and (
        "sql" in skills
        or "power bi" in skills
        or "tableau" in skills
    ):
        roles.append("Data Analyst")

    # Frontend Developer
    if (
        "html" in skills
        and "css" in skills
        and "javascript" in skills
    ):
        roles.append("Frontend Developer")

    # Full Stack Developer
    if (
        "react" in skills
        and "node.js" in skills
    ):
        roles.append("Full Stack Developer")

    # Java Developer
    if "java" in skills:
        roles.append("Java Developer")

    # Python Developer
    if "python" in skills:
        roles.append("Python Developer")

    return list(dict.fromkeys(roles))