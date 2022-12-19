import { axios } from "../../libs/axios";

export async function getWorkoutExercises(workout_id) {
    const response = await axios.get(`exercises/${workout_id}/exercises`);
    return response.data;
};

export async function getExercise(exercise_id) {
    console.log("Eexercise_id : ", exercise_id)
    const response = await axios.get(`exercises/${exercise_id}`);
    return response.data;
}