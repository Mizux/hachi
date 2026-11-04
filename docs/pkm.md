## Types Chart

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
    style Normal color:#111,fill:#C06040
    style Fire color:#111,fill:#E02020
    style Grass color:#111,fill:#20A040
    style Water color:#DDD,fill:#0080E0
    style Electric color:#111,fill:#F0F000
    style Ice color:#111,fill:#40F0F0
    style Fighting color:#111,fill:#806030
    style Poison color:#080,fill:#8000E0
    style Ground color:#111,fill:#806030
    style Flying color:#111,fill:#C08060
    style Psychic color:#111,fill:#F050A0
    style Bug color:#111,fill:#008040
    style Rock color:#111,fill:#404040
    style Ghost color:#111,fill:#D0D0D0
    style Dragon color:#111,fill:#C0E000
    style Dark color:#FF0,fill:#202020
    style Steel color:#111,fill:#808080
    style Fairy color:#111,fill:#E050C0
```

## Type Stats

| Type | Weak To (Incoming) | Strong Against (Outgoing) | 3-Type Cycles |
| :--- | :--- | :--- | :---: |
| **`Normal`** | `Fighting` (1) | *(None)* (0) | **0** |
| **`Fire`** | `Water`, `Ground`, `Rock` (3) | `Grass`, `Ice`, `Bug`, `Steel` (4) | **5** |
| **`Grass`** | `Fire`, `Ice`, `Poison`, `Flying`, `Bug` (5) | `Water`, `Ground`, `Rock` (3) | **7** |
| **`Water`** | `Grass`, `Electric` (2) | `Fire`, `Ground`, `Rock` (3) | **2** |
| **`Electric`** | `Ground` (1) | `Water`, `Flying` (2) | **1** |
| **`Ice`** | `Fire`, `Fighting`, `Rock`, `Steel` (4) | `Grass`, `Ground`, `Flying`, `Dragon` (4) | **5** |
| **`Fighting`** | `Flying`, `Psychic`, `Fairy` (3) | `Normal`, `Ice`, `Rock`, `Dark`, `Steel` (5) | **4** |
| **`Poison`** | `Ground`, `Psychic` (2) | `Grass`, `Fairy` (2) | **1** |
| **`Ground`** | `Grass`, `Water`, `Ice` (3) | `Fire`, `Electric`, `Poison`, `Rock`, `Steel` (5) | **6** |
| **`Flying`** | `Electric`, `Ice`, `Rock` (3) | `Grass`, `Fighting`, `Bug` (3) | **3** |
| **`Psychic`** | `Bug`, `Ghost`, `Dark` (3) | `Fighting`, `Poison` (2) | **1** |
| **`Bug`** | `Fire`, `Flying`, `Rock` (3) | `Grass`, `Psychic`, `Dark` (3) | **1** |
| **`Rock`** | `Grass`, `Water`, `Fighting`, `Ground`, `Steel` (5) | `Fire`, `Ice`, `Flying`, `Bug` (4) | **7** |
| **`Ghost`** | `Ghost`, `Dark` (2) | `Psychic`, `Ghost` (2) | **0** |
| **`Dragon`** | `Ice`, `Dragon`, `Fairy` (3) | `Dragon` (1) | **0** |
| **`Dark`** | `Fighting`, `Bug`, `Fairy` (3) | `Psychic`, `Ghost` (2) | **1** |
| **`Steel`** | `Fire`, `Fighting`, `Ground` (3) | `Ice`, `Rock`, `Fairy` (3) | **3** |
| **`Fairy`** | `Poison`, `Steel` (2) | `Fighting`, `Dragon`, `Dark` (3) | **1** |

## Type Cycles

Found 16 3-type cycles:

- Fire -> Grass -> Water -> Fire
- Fire -> Grass -> Ground -> Fire
- Fire -> Grass -> Rock -> Fire
- Fire -> Ice -> Ground -> Fire
- Fire -> Steel -> Rock -> Fire
- Grass -> Ground -> Poison -> Grass
- Grass -> Rock -> Ice -> Grass
- Grass -> Rock -> Flying -> Grass
- Grass -> Rock -> Bug -> Grass
- Water -> Ground -> Electric -> Water
- Ice -> Ground -> Rock -> Ice
- Ice -> Ground -> Steel -> Ice
- Ice -> Flying -> Fighting -> Ice
- Fighting -> Rock -> Flying -> Fighting
- Fighting -> Dark -> Psychic -> Fighting
- Fighting -> Steel -> Fairy -> Fighting
