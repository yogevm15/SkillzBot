# The Plan To Take Over The World
---------------------

#### <span style="color: lightblue">Definitions</span>:
##### Any words in a `single line code block` refer to things defined here
`defense range` - The distance between our and the enemy castle, halved.
```py
  game.get_my_castle().distance(game.get_enemy_castle()) / 2
```
`maayan formula` - A calculation made by Maayan to find the location for portal building

`reversed maayan formula` - A calculation made by Maayan to find the location for mana fountain building by opposing the `maayan formula` calculation

`attack mana` - <span style="color:aqua">300</span>

`defense mode` - An elf goes to attack any elf or ice troll which enters the `defense range`. the defense portal spawns one ice troll when an elf or a lava giant come close to it

`buildings` - Mana fountains and portals

#### <span style="color: lightblue">The plan</span>:
##### What are we doing?
1. Clear all enemy buildings from `defense range`
2. Build two mana fountains using the `reversed maayan formula`
3. Enter `defense mode` for both elves while waiting to reach `attack mana`
4. Assign an elf to an `attack mission`. the other one stays in `defense mode`.

#### Attack Mission Tasks:
1. Build attack portal using the `maayan formula` from the enemy castle where the radius is the highest distance of an enemy building from the enemy castle
2. While the enemy has `buildings` the attack portal spawns ice trolls and the elf who built it goes to destroy said buildings. the attacking elf should evade enemy ice trolls.
3. When the enemy has no `buildings` left the attack portal starts to spawn lava giants and the effect is irreversible (effect `balagan`).
