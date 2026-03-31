#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


BUILD_QUESTION_COUNT = 20
FOLLOWUP_COUNT = 5


def state_path(root: Path) -> Path:
    return root / ".xunxiashi" / "onboarding-state.json"


def load_state(root: Path) -> dict:
    path = state_path(root)
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(root: Path, data: dict) -> None:
    path = state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def init_state(root: Path, mode: str) -> dict:
    data = {
        "phase": "build_brain",
        "mode": mode,
        "last_completed_question": 0,
        "last_completed_followup": 0,
        "written_files": [],
        "answers": {},
        "followups": {},
    }
    save_state(root, data)
    return data


def mark_question(root: Path, number: int, answer: str, writes: list[str]) -> dict:
    data = load_state(root)
    data.setdefault("answers", {})
    data.setdefault("written_files", [])
    data["answers"][str(number)] = answer
    data["last_completed_question"] = max(number, data.get("last_completed_question", 0))
    for item in writes:
        if item not in data["written_files"]:
            data["written_files"].append(item)
    if data["last_completed_question"] >= BUILD_QUESTION_COUNT:
        data["phase"] = "post_build_config"
    save_state(root, data)
    return data


def mark_followup(root: Path, number: int, summary: str, writes: list[str]) -> dict:
    data = load_state(root)
    data.setdefault("followups", {})
    data.setdefault("written_files", [])
    data["followups"][str(number)] = summary
    data["last_completed_followup"] = max(number, data.get("last_completed_followup", 0))
    for item in writes:
        if item not in data["written_files"]:
            data["written_files"].append(item)
    if data["last_completed_followup"] >= FOLLOWUP_COUNT:
        data["phase"] = "train_brain"
    else:
        data["phase"] = "post_build_config"
    save_state(root, data)
    return data


def next_item(data: dict) -> dict:
    phase = data.get("phase", "kickoff")
    if phase == "build_brain":
        return {"phase": phase, "next_question": data.get("last_completed_question", 0) + 1}
    if phase == "post_build_config":
        return {"phase": phase, "next_followup": data.get("last_completed_followup", 0) + 1}
    return {"phase": phase}


def main() -> None:
    parser = argparse.ArgumentParser(description="Track Xunxiashi onboarding progress.")
    parser.add_argument("--root", required=True, help="Workspace root")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init")
    init_cmd.add_argument("--mode", choices=["merge", "replace"], required=True)

    q_cmd = sub.add_parser("question")
    q_cmd.add_argument("--number", type=int, required=True)
    q_cmd.add_argument("--answer", required=True)
    q_cmd.add_argument("--writes", nargs="*", default=[])

    f_cmd = sub.add_parser("followup")
    f_cmd.add_argument("--number", type=int, required=True)
    f_cmd.add_argument("--summary", required=True)
    f_cmd.add_argument("--writes", nargs="*", default=[])

    sub.add_parser("status")
    sub.add_parser("next")

    args = parser.parse_args()
    root = Path(args.root)

    if args.command == "init":
        print(json.dumps(init_state(root, args.mode), ensure_ascii=False, indent=2))
        return
    if args.command == "question":
        print(
            json.dumps(
                mark_question(root, args.number, args.answer, args.writes),
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    if args.command == "followup":
        print(
            json.dumps(
                mark_followup(root, args.number, args.summary, args.writes),
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    data = load_state(root)
    if args.command == "status":
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    if args.command == "next":
        print(json.dumps(next_item(data), ensure_ascii=False, indent=2))
        return


if __name__ == "__main__":
    main()
