#!/usr/bin/env python3
"""Генератор випадкових паролів на основі модуля secrets."""

import argparse
import secrets
import string

AMBIGUOUS = "O0oIl1|`'\""


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> str:
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?/~")

    if exclude_ambiguous:
        pools = ["".join(c for c in p if c not in AMBIGUOUS) for p in pools]

    if not pools:
        raise ValueError("Потрібно обрати хоча б один тип символів.")
    if length < len(pools):
        raise ValueError(f"Мінімальна довжина для обраних налаштувань: {len(pools)}.")

    # Гарантуємо щонайменше один символ з кожного обраного набору
    chars = [secrets.choice(p) for p in pools]
    alphabet = "".join(pools)
    chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]

    # Перемішуємо криптографічно стійким способом
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Генератор випадкових паролів")
    parser.add_argument("-l", "--length", type=int, default=16, help="довжина пароля (за замовчуванням 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="кількість паролів")
    parser.add_argument("--no-lower", action="store_true", help="без малих літер")
    parser.add_argument("--no-upper", action="store_true", help="без великих літер")
    parser.add_argument("--no-digits", action="store_true", help="без цифр")
    parser.add_argument("--no-symbols", action="store_true", help="без спецсимволів")
    parser.add_argument("--no-ambiguous", action="store_true", help="без схожих символів (O, 0, l, 1, I ...)")
    args = parser.parse_args()

    try:
        for _ in range(args.count):
            print(
                generate_password(
                    length=args.length,
                    use_lower=not args.no_lower,
                    use_upper=not args.no_upper,
                    use_digits=not args.no_digits,
                    use_symbols=not args.no_symbols,
                    exclude_ambiguous=args.no_ambiguous,
                )
            )
    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()
