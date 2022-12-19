import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
// import { CustomizedButton as Button } from "../../components/Button";
import { Container } from "@mui/system";
import { getExerciseSets } from "../../shared/api/SetAPI"
import { useParams } from "react-router-dom";
import HistoryTable from "./HistoryTable";
import { getExercise } from "../../shared/api/ExerciseAPI";

function History() {
  let { id } = useParams();
  const [sets, setSets] = useState([]);
  const [exercise, setExercise] = useState(null);

  useEffect(() => {
    const retrieveExercise = async () => {
      console.log("HERE now : ", id)
      const data = await getExercise(id);
      setExercise(data);
    };
    retrieveExercise()
    .catch(console.error);
  }, [id]);

  useEffect(() => {
    const fetchSets = async () => {
      const data = await getExerciseSets(id);
      setSets(data)
    }
    fetchSets()
      .catch(console.error);
  }, [id]);

  if (!exercise){
    return
  }

  return (
    <div className="App">
      <Container maxWidth='md'>
        <Box sx={{ boxShadow: 3, p: 2 }}>
          <h1>History for {exercise.name}</h1>
          <HistoryTable 
            sets={sets}
          />
        </Box>
      </Container>
    </div>
  );
}

export { History };