# Gym Log
This is a small web appilication that can be used to track gym progress and for recording workout information such as reps, weight and sets.
This application can be used to create workout with ease for the user to use during a workout quikcly and effectively

# Domain Model
```mermaid
    graph TD
    A[user]
    A --- D
    B[set] --- C[exercise]
    C --- D[workout]

```
#ERD
```mermaid
%%{init: {'theme': 'forest', 'themeVariables': { 'lineColor': 'white'}}}%%
erDiagram
USER {
    int id PK
    string first_name
    string last_name
    string email
    string password
}

WORKOUT {
    int id PK
    string name
    int user_id FK
}

WORKOUT_EXERCISE {
    int id PK
    int workout_id FK
    int exercise_id FK
}

EXERCISE {
    int id PK
    string name
}

SET {
    int id PK
    double weight
    int reps
    int exercise_id FK
}

USER ||--|{ WORKOUT : has
WORKOUT }|--|{ WORKOUT_EXERCISE : has
WORKOUT_EXERCISE }|--|{ EXERCISE : has
EXERCISE ||--|{ SET : has
```
