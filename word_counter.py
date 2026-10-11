#!/usr/bin/env python3
"""Лічильник слів: статистика по текстовому файлу або тексту зі stdin."""

import argparse
import re
import sys
from collections import Counter


def analyze(text: str, top: int = 10) -> None:
    words = re.findall(r"[\w'’-]+", text.lower())
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)

    print(f"Символів: {len(text)}")
    print(f"Рядків:   {lines}")
    print(f"Слів:     {len(words)}")
    print(f"Унікальних слів: {len(set(words))}")

    if words:
        avg = sum(len(w) for w in words) / len(words)
        print(f"Середня довжина слова: {avg:.2f}")
        print(f"\nТоп-{top} найчастіших слів:")
        for word, count in Counter(words).most_common(top):
            print(f"  {word:<20} {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Лічильник слів")
    parser.add_argument("file", nargs="?", help="шлях до файлу (інакше читається stdin)")
    parser.add_argument("-t", "--top", type=int, default=10, help="скільки слів показати")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    else:
        print("Введіть текст (Ctrl+D / Ctrl+Z для завершення):", file=sys.stderr)
        text = sys.stdin.read()

    analyze(text, args.top)


if __name__ == "__main__":
    main()
