def generate_suggestions(skills, education, projects, certifications):
    """
    Generates resume improvement suggestions.
    Returns a list of suggestions.
    """

    suggestions = []

    # Check Skills
    if len(skills) == 0:
        suggestions.append("Add more technical skills to your resume.")

    # Check Education
    if len(education) == 0:
        suggestions.append("Include your education details.")

    # Check Projects
    if len(projects) == 0:
        suggestions.append("Add at least one or two projects to showcase your practical experience.")

    # Check Certifications
    if len(certifications) == 0:
        suggestions.append("Add relevant certifications to strengthen your resume.")

    # Additional suggestions
    if len(skills) < 5:
        suggestions.append("Try adding more relevant technical skills.")

    if len(projects) < 2:
        suggestions.append("Include more projects to improve your profile.")

    # If everything looks good
    if len(suggestions) == 0:
        suggestions.append("Excellent! Your resume contains all the important sections.")

    return suggestions