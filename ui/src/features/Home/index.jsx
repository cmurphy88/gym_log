// import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
// import { CustomizedButton as Button } from "../../components/Button";
import { Container } from "@mui/system";
import useAuth from "../../provider/useAuth";
import Button from "@mui/material/Button";
import { WorkoutPage } from "../Workout";
import { useState } from "react";

function HomePage() {
  const [open, setOpen] = useState(false);

  const { user } = useAuth()
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  //   const [homes, setHomes] = useState()
  //   const [ setDisplayModal] = React.useState(false);

  //   useEffect(() => {
  //     // declare the data fetching function
  //     const fetchHomes = async () => {
  //       const data = await getUsersHomes(user.id);
  //       setHomes(data)
  //     }

  //     // call the function
  //     fetchHomes()
  //       // make sure to catch any error
  //       .catch(console.error);
  //   }, [user])

  return (
    <div className="App">
      <Container
        maxWidth='md'
      >
        <Box sx={{ boxShadow: 3, p: 2 }}>
          <Box>
            <h1>Welcome {user.first_name}</h1>
          </Box>
          <Box>
            <WorkoutPage />
          </Box>
          <Box sx={{ p: 2 }}>
            <Button
              variant="contained"
              color="success"
              onClick={{ handleOpen }}
            >
              start new session
            </Button>
          </Box>
        </Box>
      </Container>
    </div>
  );
}

export { HomePage };