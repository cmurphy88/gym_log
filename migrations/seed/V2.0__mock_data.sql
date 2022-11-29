INSERT INTO users (first_name, last_name, email, password)
    VALUES ('Conor', 'Murphy', 'conor@g.com', '$argon2id$v=19$m=65536,t=3,p=4$ZixlbE3pfa9VylmrVaq1Ng$Hdn4GZi8xj0Lu5DJOF8m8RtCOuFk0IWfx9rzDQABBnk');

INSERT INTO workout (name, user_id)
    VALUES ('Chest', 1);

INSERT INTO exercise (name)
    VALUES ('Bench Press');

INSERT INTO workout_exercise (workout_id, exercise_id)
    VALUES (1, 1);

INSERT INTO set (weight, reps, exercise_id)
    VALUES (80.0, 8, 1);