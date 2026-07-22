def calculate_ats_score(skills, education, projects, certifications):
    """
    Calculates the ATS score based on the available resume sections.
    Returns the total score.
    """

    score = 0

    # Skills (40 marks)
    if len(skills) > 0:
        score += 40

    # Education (20 marks)
    if len(education) > 0:
        score += 20

    # Projects (20 marks)
    if len(projects) > 0:
        score += 20

    # Certifications (20 marks)
    if len(certifications) > 0:
        score += 20

    return score