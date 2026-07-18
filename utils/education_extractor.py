def extract_education(text):
    """
    Extracts education details from the resume text.
    Returns a list of education-related lines.
    """

    education_keywords = [
        "b.tech",
        "b.e",
        "b.sc",
        "bca",
        "m.tech",
        "m.e",
        "m.sc",
        "mca",
        "phd",
        "bachelor",
        "master",
        "degree",
        "diploma",
        "college",
        "university",
        "institute",
        "school",
        "cgpa",
        "gpa",
        "percentage"
    ]

    education_details = []

    # Split resume text into lines
    lines = text.splitlines()

    # Check every line
    for line in lines:
        line = line.strip()

        for keyword in education_keywords:
            if keyword in line.lower():
                education_details.append(line)
                break

    return list(dict.fromkeys(education_details))