#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(item in lowered for item in allowed):
        return f"{ingredients} -> VALID"
    else:
        return f"{ingredients} -> INVALID"


# ファイルの冒頭で
# from .light_spellbook import light_spell_allowed_ingredients
# これを描いてしまうと、light_spellbook.pyとlight_validator.py
# の間で相互にimportしあって循環依存の関係になる。
# これを解決する方法は以下の３通りある。

# 1.関数内でimportする。
# def validate_ingredients(ingredients: str) -> str:
#     from .light_spellbook import light_spell_allowed_ingredients
# moduleが最初に読み込まれる瞬間には相手をimportしなくなるので循環を回避

# 2.1方向だけの依存にする。
# 例えば、light_validator.pyは独立させ、許可材料のリストは
# light_spell_allowed_ingredients()を使用するのではなく
# ["earth", "air", "fire", "water"] 直接これを使ってimportを回避

# 3.alchemy/grimoire/__init__.py経由でまとめる
# alchemy/grimoire/__init__.pyに両方をimportしておき、各ファイルは
# お互いをimportしない設計にする。
