| A \ D  | Normal |  Fire  | Grass  | Water  | Electric |  Ice   | Fighting | Poison | Ground | Flying | Psychic |  Bug   |  Rock  | Ghost  | Dragon |  Dark  | Steel  | Fairy  |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Normal |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |
|  Fire  |   .    |   .    |   X    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |
| Grass  |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |
| Water  |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |
| Electric |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |
|  Ice   |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   X    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |
| Fighting |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   X    |   X    |   .    |
| Poison |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |
| Ground |   .    |   X    |   .    |   .    |   X    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   X    |   .    |
| Flying |   .    |   .    |   X    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |
| Psychic |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |
|  Bug   |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |
|  Rock  |   .    |   X    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   X    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |
| Ghost  |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |
| Dragon |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |
|  Dark  |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |
| Steel  |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   X    |
| Fairy  |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   .    |   .    |   .    |   .    |   .    |   .    |   .    |   X    |   X    |   .    |   .    |

```mermaid
flowchart TD
    Normal[Normal]
    Fire[Fire]
    Grass[Grass]
    Water[Water]
    Electric[Electric]
    Ice[Ice]
    Fighting[Fighting]
    Poison[Poison]
    Ground[Ground]
    Flying[Flying]
    Psychic[Psychic]
    Bug[Bug]
    Rock[Rock]
    Ghost[Ghost]
    Dragon[Dragon]
    Dark[Dark]
    Steel[Steel]
    Fairy[Fairy]
    Fire --> Grass
    Fire --> Ice
    Fire --> Bug
    Fire --> Steel
    Grass --> Water
    Grass --> Ground
    Grass --> Rock
    Water --> Fire
    Water --> Ground
    Water --> Rock
    Electric --> Water
    Electric --> Flying
    Ice --> Grass
    Ice --> Ground
    Ice --> Flying
    Ice --> Dragon
    Fighting --> Normal
    Fighting --> Ice
    Fighting --> Rock
    Fighting --> Dark
    Fighting --> Steel
    Poison --> Grass
    Poison --> Fairy
    Ground --> Fire
    Ground --> Electric
    Ground --> Poison
    Ground --> Rock
    Ground --> Steel
    Flying --> Grass
    Flying --> Fighting
    Flying --> Bug
    Psychic --> Fighting
    Psychic --> Poison
    Bug --> Grass
    Bug --> Psychic
    Bug --> Dark
    Rock --> Fire
    Rock --> Ice
    Rock --> Flying
    Rock --> Bug
    Ghost --> Psychic
    Ghost --> Ghost
    Dragon --> Dragon
    Dark --> Psychic
    Dark --> Ghost
    Steel --> Ice
    Steel --> Rock
    Steel --> Fairy
    Fairy --> Fighting
    Fairy --> Dragon
    Fairy --> Dark
    style Normal fill:#C06040
    style Fire fill:#E00000
    style Grass fill:#00E000
    style Water fill:#0000E0
    style Electric fill:#F0F000
    style Ice fill:#40F0F0
    style Fighting fill:#806030
    style Poison fill:#8000E0
    style Ground fill:#806030
    style Flying fill:#C08060
    style Psychic fill:#FF8000
    style Bug fill:#008040
    style Rock fill:#404040
    style Ghost fill:#D0D0D0
    style Dragon fill:#C0E000
    style Dark fill:#202020
    style Steel fill:#808080
    style Fairy fill:#E050C0
```
