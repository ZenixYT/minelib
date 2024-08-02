execute as @s store result score $bedX BedSpawn run data get entity @s SpawnX
execute as @s store result score $bedY BedSpawn run data get entity @s SpawnY
execute as @s store result score $bedZ BedSpawn run data get entity @s SpawnZ
summon minecraft:area_effect_cloud 0 10000 0 {"Tags": ["MAGIC_MIRROR_REF"]}
execute as @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] store result entity @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] Pos[0] double 1 run scoreboard players get $bedX BedSpawn
execute as @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] store result entity @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] Pos[1] double 1 run scoreboard players get $bedY BedSpawn
execute as @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] store result entity @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}] Pos[2] double 1 run scoreboard players get $bedZ BedSpawn
execute as @s run tp @s @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}]
kill @e[nbt={"Tags": ["MAGIC_MIRROR_REF"]}]
scoreboard players set $bedX BedSpawn 0
scoreboard players set $bedY BedSpawn 0
scoreboard players set $bedZ BedSpawn 0