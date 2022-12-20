import { Box, Button } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { getUsersWorkouts } from "../../shared/api/WorkoutAPI";
import useAuth from "../../provider/useAuth";
import WorkoutAccordian from "./WorkoutAccordion";
import CreateWorkoutModal from "./CreateWorkoutModal";

function WorkoutPage() {
  const { user } = useAuth();
  const [workouts, setWorkouts] = useState();
  const [displayModal, setDisplayModal] = useState(false);


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
        <Box >
          <h2>Your Workouts</h2>
          <Container>
            {workouts && workouts.map((w, i) => {
              return <WorkoutAccordian key={w.id} workout={w} />
            })}
          </Container>
          <Box>
            <Button
              variant="contained"
              sx={{ m: 1 }}
              onClick={() => setDisplayModal(true)}
            >
              Create new Workout
            </Button>
          </Box>
          <Box>
            <CreateWorkoutModal
              // roomId={id}
              isOpen={displayModal}
              handleClose={() => {
                setDisplayModal(false);
              }}
            />
          </Box>
        </Box>
      </Container>
    </div>
  );
}

export { WorkoutPage };