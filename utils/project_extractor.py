def extract_projects(text):
    """
    Extracts project details from the resume text.
    Returns a list of project-related lines.
    """

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented",
        "created",
        "designed"
    ]

    project_details = []

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        for keyword in project_keywords:
            if keyword in line.lower():
                project_details.append(line)
                break

    return list(dict.fromkeys(project_details))