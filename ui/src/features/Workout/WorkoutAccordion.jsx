import React, { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { Button, ListItemButton, ListItemText } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { getWorkoutExercises } from '../../shared/api/ExerciseAPI';
import AddExerciseModal from '../Exercise/AddExerciseModal';



export default function WorkoutAccordian({ workout }) {
    const [exercises, setExercises] = useState()
    const [open, setOpen] = useState(false);
    const [displayModal, setDisplayModal] = useState(false);
    const navigate = useNavigate()

    useEffect(() => {
        const fetchExercises = async () => {
            const data = await getWorkoutExercises(workout.id);
            setExercises(data)
        }
        fetchExercises()
            .catch(console.error);
    }, [workout.id])


    return (
        <Accordion>
            <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
            >
                <Typography> {workout.name} </Typography>
            </AccordionSummary>
            <AccordionDetails>
                {exercises && exercises.map((e, i) => {
                    return <ListItemButton key={i} onClick={() => navigate(`/exercises/${e.id}/history`)}>
                        <ListItemText primary={e.name}>{e.name}</ListItemText>
                    </ListItemButton>
                })}
                <AddExerciseModal
                    isOpen={displayModal}
                    handleClose={() => {
                        setDisplayModal(false);
                    }}
                />
            </AccordionDetails>

        </Accordion>
    );
}
