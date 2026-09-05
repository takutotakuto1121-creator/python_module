#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda item: item['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[dict]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda item: item['power'])
    min_power = min(mages, key=lambda item: item['power'])
    avg_power = round(sum(m['power'] for m in mages) / len(mages), 2)
    return {
        'max_power': max_power, 'min_power': min_power,
        'avg_power': avg_power}


if __name__ == '__main__':
    artifacts = [
        {'name': 'Shadow Blade', 'power': 82, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 94, 'type': 'accessory'},
        {'name': 'Earth Shield', 'power': 74, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}
        ]

    mages = [
        {'name': 'River', 'power': 82, 'element': 'light'},
        {'name': 'Morgan', 'power': 100, 'element': 'earth'},
        {'name': 'Zara', 'power': 79, 'element': 'fire'},
        {'name': 'Kai', 'power': 93, 'element': 'wind'},
        {'name': 'Storm', 'power': 78, 'element': 'light'}
        ]

    spells = ['tornado', 'tsunami', 'lightning', 'meteor']

    print("= Testing artifact_sorter() =")
    print(artifact_sorter(artifacts))
    print()

    print('= Testing power_filter() =')
    min_power = 90
    print(power_filter(mages, min_power))
    print()

    print('= Testing spell_transformer() =')
    print(spell_transformer(spells))
    print()

    print('= Testing mage_stats() =')
    print(mage_stats(mages))
