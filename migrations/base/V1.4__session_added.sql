ALTER TABLE set DROP COLUMN date;

CREATE TABLE session (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date DATE
);

ALTER TABLE set ADD session_id int;
ALTER TABLE set ADD CONSTRAINT fk_set_session_session_id FOREIGN KEY (session_id)
    REFERENCES session(id);