CREATE TABLE users
(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email           VARCHAR(50),
    password        VARCHAR(255)
);

CREATE TABLE workout
(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30),
    user_id INT,
    CONSTRAINT fk_workout_user_user_id FOREIGN KEY (user_id)
        REFERENCES users(id)
);

CREATE TABLE exercise
(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30)
);

CREATE TABLE workout_exercise
(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    workout_id INT,
    exercise_id INT,
    CONSTRAINT fk_workout_exercise_workout_workout_id FOREIGN KEY (workout_id)
        REFERENCES workout(id),
    CONSTRAINT fk_workout_exercise_workout_exercise_id FOREIGN KEY (exercise_id)
        REFERENCES exercise(id)
);

CREATE TABLE set
(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    weight DECIMAL(10, 2),
    reps INT,
    exercise_id INT,
    CONSTRAINT fk_set_exercise_exercise_id FOREIGN KEY (exercise_id)
        REFERENCES exercise(id)
)