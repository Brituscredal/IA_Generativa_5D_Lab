#!/usr/bin/env python
import sys
from pathlib import Path


def parse_pairs(pairs):
    values = {}
    for raw in pairs:
        if "=" not in raw:
            raise ValueError(f"Par invalido: {raw}. Use CHAVE=valor")
        key, value = raw.split("=", 1)
        key = key.strip()
        if key.startswith("{") and key.endswith("}"):
            key = key[1:-1].strip()
        if not key:
            raise ValueError(f"Chave vazia em: {raw}")
        values[key] = value
    return values


def render_template(template_text, values):
    rendered = template_text
    for key, value in values.items():
        rendered = rendered.replace("{" + key + "}", value)
    return rendered


def main(argv):
    if len(argv) < 2:
        print("Uso: prompt_runner <template_path> CHAVE=valor [CHAVE=valor ...]")
        return 2

    template_path = Path(argv[0])
    if not template_path.exists():
        print(f"Template nao encontrado: {template_path}")
        return 2

    try:
        values = parse_pairs(argv[1:])
    except ValueError as exc:
        print(str(exc))
        return 2

    template_text = template_path.read_text(encoding="utf-8")
    output = render_template(template_text, values)
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

# Teste manual (PowerShell):
# python .\src\prompt_runner.py .\prompts\aula03_skeleton.md OBJETIVO="AAA" TEMA="BBB" NIVEL="CCC" > out\render_teste.md
