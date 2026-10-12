from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()
print("jsdfkjsdafjkdsafjkdsa")
engine = create_engine(os.environ["DATABASE_URL"])

with engine.connect() as conn:
    rows = conn.execute(
        text("""
            SELECT
                t.Id,
                t.ProjectName,
                t.Description,
                t.Level,
                l.Name AS LevelName
            FROM dbo.PMRagTool t
            INNER JOIN dbo.PMRagToolLevel l
                ON t.Level = l.Id
            WHERE t.ProjectName = :project_name
            ORDER BY t.Id
        """),
        {"project_name": "PeopleManager"},
    ).fetchall()

    if not rows:
        print("No PeopleManager records found.")
    else:
        for row in rows:
            print(f"\nID: {row.Id}")
            print(f"Project: {row.ProjectName}")
            print(f"Level: {row.LevelName} (ID: {row.Level})")
            print(f"Description: {row.Description}")
            print("-" * 80)