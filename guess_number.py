#!/usr/bin/env python3
"""Гра «Вгадай число»."""

import random


def play(low: int = 1, high: int = 100, max_attempts: int = 7) -> None:
    secret = random.randint(low, high)
    print(f"Я загадав число від {low} до {high}. У вас {max_attempts} спроб.")

    for attempt in range(1, max_attempts + 1):
        while True:
            raw = input(f"Спроба {attempt}/{max_attempts}: ").strip()
            try:
                guess = int(raw)
                break
            except ValueError:
                print("Введіть ціле число.")

        if guess == secret:
            print(f"Вгадали за {attempt} спроб(и)!")
            return
        print("Більше." if guess < secret else "Менше.")

    print(f"Спроби закінчилися. Було загадано: {secret}")


def main() -> None:
    while True:
        play()
        if input("Ще раз? (т/н): ").strip().lower() not in ("т", "y", "так", "yes"):
            print("До зустрічі!")
            break


if __name__ == "__main__":
    main()
