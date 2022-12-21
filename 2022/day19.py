import re
import math

input_data = open("inputs/day19.in", "r").read().strip().split("\n")

recipes = [tuple(map(int, re.findall(r"-?\d+", line))) for line in input_data]


def get_geodes(recipe, ticks):
    queue = [(1, 0, 0, 0, 0, 0, 0, 0, 0)]
    seen = {(1, 0, 0, 0, 0, 0, 0, 0)}
    while queue:
        (
            ore_bot,
            clay_bot,
            obsidian_bot,
            geode_bot,
            ore,
            clay,
            obsidian,
            geode,
            tick,
        ) = queue.pop(0)
        if ore > (ticks - tick) * max(recipe[1], recipe[2], recipe[3], recipe[5]):
            ore = (ticks - tick) * max(recipe[1], recipe[2], recipe[3], recipe[5])
        if clay > (ticks - tick) * recipe[4]:
            clay = (ticks - tick) * recipe[4]
        if obsidian > (ticks - tick) * recipe[6]:
            obsidian = (ticks - tick) * recipe[6]

        if tick >= ticks:
            return geode

        possibilities = [
            (
                ore_bot + oreb,
                clay_bot + clayb,
                obsidian_bot + obsib,
                geode_bot + geob,
                ore + ore_bot + ore_cost,
                clay + clay_bot + clay_cost,
                obsidian + obsidian_bot + obsidian_cost,
                geode + geode_bot,
                tick + 1,
            )
            for oreb, clayb, obsib, geob, ore_cost, clay_cost, obsidian_cost in get_alternatives(
                recipe, ore, clay, obsidian, ore_bot, clay_bot, obsidian_bot
            )
        ]
        new_states = [new for new in possibilities if new[:-1] not in seen]
        queue = sorted(
            queue + new_states,
            key=lambda x: (
                sum(x[3] + t for t in range(ticks - x[8])) + x[7],
                x[2],
                x[0],
                x[1],
            ),
            reverse=True,
        )[:10000]
        seen.update(new[:-1] for new in new_states)
    return None


def get_alternatives(recipe, ore, clay, obsidian, ore_bot, clay_bot, obsidian_bot):
    alternatives = set()
    if ore >= recipe[1] and ore_bot < max(recipe[1], recipe[2], recipe[3], recipe[5]):
        alternatives.add((1, 0, 0, 0, -recipe[1], 0, 0))
    if ore >= recipe[2] and clay_bot < recipe[4]:
        alternatives.add((0, 1, 0, 0, -recipe[2], 0, 0))
    if ore >= recipe[3] and clay >= recipe[4] and obsidian_bot < recipe[6]:
        alternatives.add((0, 0, 1, 0, -recipe[3], -recipe[4], 0))
    if ore >= recipe[5] and obsidian >= recipe[6]:
        alternatives.add((0, 0, 0, 1, -recipe[5], 0, -recipe[6]))
    else:
        alternatives.add((0, 0, 0, 0, 0, 0, 0))
    return alternatives


# Note: This code is trash and takes hours, but I'm tired of graphsearches
# Improvement would be to disregard waiting steps and add cost of waiting for different robots
print("Part 1:", sum(recipe[0] * get_geodes(recipe, 24) for recipe in recipes))
print("Part 2:", math.prod(get_geodes(recipe, 32) for recipe in recipes[:3]))
