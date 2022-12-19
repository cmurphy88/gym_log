import { Box } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { getUsersWorkouts } from "../../shared/api/WorkoutAPI";
import useAuth from "../../provider/useAuth";
import WorkoutAccordian from "./WorkoutAccordion";

function WorkoutPage() {
    const { user } = useAuth();
    const [workouts, setWorkouts] = useState();

    useEffect(() => {
        const fetchWorkouts = async () => {
            const data = await getUsersWorkouts(user.id);
            setWorkouts(data);
        }
        fetchWorkouts()
        .catch(console.error)
    }, [user])
  
    return (
      <div className="App">
        <Container maxWidth='md'>
          <Box sx={{ boxShadow: 3, p: 2 }}>
            <h2>Workouts</h2>
            <Container>
                {workouts && workouts.map((w, i) => {
                    return <WorkoutAccordian key={w.id} workout ={w}/>
                })}
            </Container>
          </Box>
        </Container>
      </div>
    );
  }
  
  export { WorkoutPage };