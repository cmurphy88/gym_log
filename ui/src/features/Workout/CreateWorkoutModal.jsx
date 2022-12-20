import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { Controller, useForm } from 'react-hook-form';
import { Alert, TextField } from '@mui/material';
import { createNewWorkout } from '../../shared/api/WorkoutAPI';
import useAuth from '../../provider/useAuth';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function CreateWorkoutModal(props) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const { handleSubmit, control } = useForm();
  const { user } = useAuth();
  const [displayModal, setDisplayModal] = React.useState(false);


  const addNewWorkout = (formData) => createNewWorkout(formData.workout_name, user.id);

  return (
    <div>
      <Modal
        open={props.isOpen}
        onClose={props.handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Create new workout
          </Typography>
          <div>
            <Controller
              name="workout_name"
              control={control}
              defaultValue=""
              rules={{ required: "Name required" }}
              render={({
                field: { onChange, value },
                fieldState: { error },
              }) => (
                <TextField
                  id="outlined-name"
                  label="Workout"
                  type="text"
                  value={value}
                  onChange={onChange}
                  variant="standard"
                  margin="dense"
                  error={!!error}
                  helperText={error ? error.message : null}
                  required
                />
              )}
            />
          </div>
          <Button
            variant='contained'
            sx={{ marginTop: 5 }}
            onClick={
              handleSubmit(addNewWorkout)
            }
          >
            Submit
          </Button>

          {/* <Alert severity="success">This is a success alert — check it out!</Alert> */}
          <Button
            onClick={handleClose}
            variant='contained'
            sx={{ marginTop: 5, marginLeft: 5 }}
          >
            Cancel
          </Button>
        </Box>
      </Modal>
    </div>
  );
}