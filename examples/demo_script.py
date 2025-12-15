from pathlib import Path

from src.importer import import_data
from src.utils import kb_to_conditions
from src.symptom import parse_symptoms
from src.analyzer import Analyzer
from src.io_export import export_results_json, export_results_txt
from src.persistence import save_state, load_state


def main() -> None:
    # 1) Create a tiny dataset on the fly (CSV)
    demo_dir = Path("demo_out")
    demo_dir.mkdir(exist_ok=True)
    csv_path = demo_dir / "kb.csv"
    csv_path.write_text(
        "condition,symptoms,self_care,seek_care\n"
        'Influenza,"fever,cough,fatigue","Rest + fluids","Seek care if breathing issues"\n'
        'Common Cold,"cough,congestion,sore throat","Hydrate + rest","Seek care if severe or >7 days"\n',
        encoding="utf-8",
    )

    # 2) Import dataset
    result = import_data(csv_path)
    print(result.message)
    if result.errors:
        print("Non-fatal import issues:", result.errors[:3])
    if not result.ok or result.data is None:
        raise RuntimeError("Demo stopped: import failed.")

    # 3) Analyze symptoms
    kb = result.data
    conditions = kb_to_conditions(kb)
    user_symptoms = parse_symptoms("fever, cough")
    analyzer = Analyzer(conditions)
    analysis = analyzer.analyze(user_symptoms, top_n=2)
    print("Top results:", [r["condition"] for r in analysis["ranked_conditions"]])

    # 4) Export
    json_report = export_results_json(analysis, demo_dir / "report.json")
    txt_report = export_results_txt(analysis, demo_dir / "report.txt")
    print("Exported:", json_report, txt_report)

    # 5) Save + Load state
    state_path = save_state(demo_dir / "state.json", user_symptoms, conditions)
    loaded_symptoms, loaded_conditions = load_state(state_path)
    print("Reloaded symptoms:", [s.name for s in loaded_symptoms])
    print("Reloaded conditions:", len(loaded_conditions))


if __name__ == "__main__":
    main()
