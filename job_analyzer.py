import csv

print("Freelance Job Analyzer")


# Your current skills
MY_SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Data Analysis",
    "Canva",
    "Social Media",
    "Content Creation"
]


# Skills the analyzer can detect in job descriptions
SKILL_KEYWORDS = [
    "Python",
    "SQL",
    "Excel",
    "Data Analysis",
    "Canva",
    "Social Media",
    "Content Creation",
    "Java",
    "JavaScript",
    "React",
    "Node.js",
    "Photoshop",
    "Illustrator",
    "Figma",
    "Machine Learning"
]


def get_job():
    job_title = input("Enter your job title: ")
    job_des = input("Enter your job description: ")

    while True:
        try:
            budget = int(input("Enter budget: "))

            if budget < 0:
                print("Budget cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            deadline = int(input("Enter deadline (in days): "))

            if deadline <= 0:
                print("Deadline must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    job = {
        "Title": job_title,
        "Description": job_des,
        "Budget": budget,
        "Deadline": deadline
    }

    return job


def analyze_budget(job):
    if job["Budget"] >= 10000:
        return 3
    elif job["Budget"] >= 5000:
        return 2
    elif job["Budget"] >= 2000:
        return 1
    else:
        return 0


def analyze_deadline(job):
    if job["Deadline"] >= 7:
        return 2
    elif job["Deadline"] >= 4:
        return 1
    else:
        return 0


def detect_skills(job):
    skills = []
    description = job["Description"].lower()

    for skill in SKILL_KEYWORDS:
        if skill.lower() in description:
            skills.append(skill)

    return skills


def match_my_skills(job):
    matched_skills = []
    description = job["Description"].lower()

    for skill in MY_SKILLS:
        if skill.lower() in description:
            matched_skills.append(skill)

    return matched_skills


def detect_red_flags(job):
    red_flags = []
    description = job["Description"].lower()

    if job["Budget"] < 2000:
        red_flags.append("Very low budget")

    if job["Deadline"] <= 2:
        red_flags.append("Very tight deadline")

    if "urgent" in description:
        red_flags.append("Urgent project")

    if "free sample" in description or "free work" in description:
        red_flags.append("Requests free work")

    if "exposure" in description:
        red_flags.append("Offers exposure instead of proper payment")

    if "unlimited revisions" in description:
        red_flags.append("Unlimited revisions")

    return red_flags


def analyze_workload(job):
    description = job["Description"].lower()

    if (
        "daily" in description
        or "multiple posts" in description
        or "long term" in description
        or "full time" in description
    ):
        return 0
    else:
        return 1


def get_workload_status(job):
    description = job["Description"].lower()

    if (
        "daily" in description
        or "multiple posts" in description
        or "long term" in description
        or "full time" in description
    ):
        return "High Workload"
    else:
        return "Normal Workload"


def analyze_clarity(job):
    description = job["Description"]

    if len(description) >= 100:
        return 2
    elif len(description) >= 50:
        return 1
    else:
        return 0


def get_recommendation(score, match_percentage):
    if match_percentage == 0:
        return "DON'T APPLY"
    elif score >= 8 and match_percentage >= 60:
        return "APPLY"
    elif score >= 5 and match_percentage >= 30:
        return "MAYBE"
    else:
        return "DON'T APPLY"


def analyze_job(job):
    score = 0
    reasons = []

    # Budget analysis
    budget_score = analyze_budget(job)
    score = score + budget_score

    if budget_score >= 2:
        reasons.append("Good budget")
    elif budget_score == 1:
        reasons.append("Average budget")
    else:
        reasons.append("Low budget")

    # Deadline analysis
    deadline_score = analyze_deadline(job)
    score = score + deadline_score

    if deadline_score == 2:
        reasons.append("Reasonable deadline")
    elif deadline_score == 1:
        reasons.append("Moderate deadline")
    else:
        reasons.append("Very tight deadline")

    # Skill analysis
    skills = detect_skills(job)
    matched_skills = match_my_skills(job)

    skill_score = min(len(matched_skills), 2)
    score = score + skill_score

    if matched_skills:
        reasons.append(
            "Your skills match: " + ", ".join(matched_skills)
        )
    else:
        reasons.append("No matching skills detected")

    # Skill match percentage
    if skills:
        match_percentage = (
            len(matched_skills) / len(skills)
        ) * 100
    else:
        match_percentage = 0

    # Workload analysis
    workload_score = analyze_workload(job)
    score = score + workload_score

    if workload_score == 1:
        reasons.append("Normal workload")
    else:
        reasons.append("High workload")

    # Clarity analysis
    clarity_score = analyze_clarity(job)
    score = score + clarity_score

    if clarity_score == 2:
        reasons.append("Clear job description")
    elif clarity_score == 1:
        reasons.append("Moderately clear job description")
    else:
        reasons.append("Short or unclear job description")

    # Red flag analysis
    red_flags = detect_red_flags(job)

    score = score - min(len(red_flags), 2)

    for flag in red_flags:
        reasons.append("Red flag: " + flag)

    if score < 0:
        score = 0

    # Final recommendation
    recommendation = get_recommendation(
        score,
        match_percentage
    )

    return {
        "Job": job,
        "Score": score,
        "Skills": skills,
        "Matched Skills": matched_skills,
        "Match Percentage": match_percentage,
        "Workload": get_workload_status(job),
        "Red Flags": red_flags,
        "Reasons": reasons,
        "Recommendation": recommendation
    }


def analyze_multiple_jobs():
    jobs = []

    while True:
        job = get_job()

        result = analyze_job(job)

        jobs.append(result)

        choice = input(
            "\nDo you want to add another job? (yes/no): "
        ).lower()

        if choice != "yes":
            break

    return jobs


def find_best_job(jobs):
    best_job = jobs[0]

    for job in jobs:
        if job["Score"] > best_job["Score"]:
            best_job = job

    return best_job


def save_to_csv(jobs):
    with open(
        "jobs_analysis.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Job Title",
            "Budget",
            "Deadline",
            "Score",
            "Skills",
            "Matched Skills",
            "Match Percentage",
            "Workload",
            "Red Flags",
            "Recommendation"
        ])

        for result in jobs:
            writer.writerow([
                result["Job"]["Title"],
                result["Job"]["Budget"],
                result["Job"]["Deadline"],
                result["Score"],
                ", ".join(result["Skills"]),
                ", ".join(result["Matched Skills"]),
                round(result["Match Percentage"]),
                result["Workload"],
                ", ".join(result["Red Flags"]),
                result["Recommendation"]
            ])


def main():

    while True:

        print("\n========================================")
        print("         FREELANCE JOB ANALYZER")
        print("========================================")
        print("1. Analyze Jobs")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            all_jobs = analyze_multiple_jobs()

            print("\n=================================")
            print("          JOB COMPARISON")
            print("=================================")

            for i, result in enumerate(all_jobs, start=1):

                print(f"\nJob {i}: {result['Job']['Title']}")
                print("Score:", result["Score"], "/10")
                print(
                    "Recommendation:",
                    result["Recommendation"]
                )

                print("Detected Skills:", end=" ")

                if result["Skills"]:
                    print(", ".join(result["Skills"]))
                else:
                    print("None")

                print("Your Matching Skills:", end=" ")

                if result["Matched Skills"]:
                    print(
                        ", ".join(result["Matched Skills"])
                    )
                else:
                    print("None")

                print(
                    "Skill Match:",
                    round(result["Match Percentage"]),
                    "%"
                )

                print("Reasons:")

                for reason in result["Reasons"]:
                    print("-", reason)

            best_job = find_best_job(all_jobs)

            print("\n=================================")
            print("            BEST JOB")
            print("=================================")

            print("Title:", best_job["Job"]["Title"])
            print("Budget:", best_job["Job"]["Budget"])
            print(
                "Deadline:",
                best_job["Job"]["Deadline"],
                "days"
            )

            if best_job["Skills"]:
                print(
                    "Skills:",
                    ", ".join(best_job["Skills"])
                )
            else:
                print("Skills: None detected")

            print("Your Matching Skills:", end=" ")

            if best_job["Matched Skills"]:
                print(
                    ", ".join(best_job["Matched Skills"])
                )
            else:
                print("None")

            print(
                "Skill Match:",
                round(best_job["Match Percentage"]),
                "%"
            )

            print("Workload:", best_job["Workload"])
            print("Score:", best_job["Score"], "/10")
            print(
                "Recommendation:",
                best_job["Recommendation"]
            )

            print("\nWhy this job:")

            for reason in best_job["Reasons"]:
                print("-", reason)

            save_to_csv(all_jobs)

            print(
                "\nResults saved to jobs_analysis.csv"
            )

        elif choice == "2":

            print(
                "\nThank you for using "
                "Freelance Job Analyzer!"
            )
            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter 1 or 2."
            )


main()