#!/usr/bin/env python3
"""Консольний список завдань, що зберігається у файлі todo.json."""

import argparse
import json
from pathlib import Path

DB = Path("todo.json")


def load() -> list[dict]:
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8"))
    return []


def save(tasks: list[dict]) -> None:
    DB.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def cmd_add(args) -> None:
    tasks = load()
    tasks.append({"text": " ".join(args.text), "done": False})
    save(tasks)
    print(f"Додано завдання №{len(tasks)}.")


def cmd_list(_args) -> None:
    tasks = load()
    if not tasks:
        print("Список порожній.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['text']}")


def cmd_done(args) -> None:
    tasks = load()
    if not 1 <= args.number <= len(tasks):
        raise SystemExit("Такого завдання немає.")
    tasks[args.number - 1]["done"] = True
    save(tasks)
    print("Позначено як виконане.")


def cmd_remove(args) -> None:
    tasks = load()
    if not 1 <= args.number <= len(tasks):
        raise SystemExit("Такого завдання немає.")
    removed = tasks.pop(args.number - 1)
    save(tasks)
    print(f"Видалено: {removed['text']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Простий список завдань")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="додати завдання")
    p_add.add_argument("text", nargs="+")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="показати завдання")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="позначити виконаним")
    p_done.add_argument("number", type=int)
    p_done.set_defaults(func=cmd_done)

    p_rm = sub.add_parser("remove", help="видалити завдання")
    p_rm.add_argument("number", type=int)
    p_rm.set_defaults(func=cmd_remove)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
