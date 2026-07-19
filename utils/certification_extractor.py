def extract_certifications(text):
    """
    Extracts certification details from the resume text.
    Returns a list of certification-related lines.
    """

    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified",
        "google",
        "aws",
        "microsoft",
        "ibm",
        "oracle",
        "coursera",
        "udemy",
        "nptel"
    ]

    certification_details = []

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        for keyword in certification_keywords:
            if keyword in line.lower():
                certification_details.append(line)
                break

    return list(dict.fromkeys(certification_details))