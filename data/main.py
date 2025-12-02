import pandas as pd

def load_domains(path: str = "data/domains.csv") -> pd.DataFrame:
    # Read CSV
    df = pd.read_csv(path)

    # Convert "skills" string -> list of clean skills
    df["skills_list"] = df["skills"].apply(
        lambda x: [s.strip().lower() for s in str(x).split("|")]
    )
    return df

def jaccard_similarity(set_a, set_b) -> float:
    """Jaccard similarity between two sets."""
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union != 0 else 0.0

def recommend_domains(user_skills, df, top_k: int = 3):
    user_skill_set = {s.strip().lower() for s in user_skills}
    scores = []

    for _, row in df.iterrows():
        domain_skills = set(row["skills_list"])
        score = jaccard_similarity(user_skill_set, domain_skills)
        scores.append((row["domain"], score, domain_skills))

    # Sort domains by similarity score (descending)
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]

def main():
    print("=== Internship Domain Recommendation Engine ===\n")

    # Load domain data
    df = load_domains()

    print("Enter your skills (comma separated)")
    print("Example: python, statistics, html, css\n")
    skills_input = input("Your skills: ")

    # Process user input
    user_skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    if not user_skills:
        print("\nNo skills entered. Please run again and enter at least one skill.")
        return

    # Get top 3 recommendations
    recommendations = recommend_domains(user_skills, df, top_k=3)

    print("\nTop recommended domains for you:\n")
    for domain, score, domain_skills in recommendations:
        print(f"- {domain} (match score: {score:.2f})")
        print(f"  Domain skills: {', '.join(domain_skills)}")
    print("\nDemo complete. You can show this output in the internship review.")

if __name__ == "__main__":
    main()
