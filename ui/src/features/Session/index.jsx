// import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
// import { CustomizedButton as Button } from "../../components/Button";
import { Container } from "@mui/system";
import useAuth from "../../provider/useAuth";
import Button from "@mui/material/Button";

function SessionPage() {
  const { user } = useAuth()
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
                <Button 
                    variant="contained"
                    color="success"
                    href="/workouts">
                        Start new Session
                </Button>
            </Box>
        </Box>
      </Container>
    </div>
  );
}

export { SessionPage };