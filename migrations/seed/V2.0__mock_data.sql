INSERT INTO users (first_name, last_name, email, password)
    VALUES ('Conor', 'Murphy', 'conor@g.com', 'password');

INSERT INTO workout (name, user_id)
    VALUES ('Chest', 1);

INSERT INTO exercise (name)
    VALUES ('Bench Press');

INSERT INTO workout_exercise (workout_id, exercise_id)
    VALUES (1, 1);

INSERT INTO set (weight, reps, exercise_id)
    VALUES (80.0, 8, 1);