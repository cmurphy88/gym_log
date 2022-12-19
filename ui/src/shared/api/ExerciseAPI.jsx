import { axios } from "../../libs/axios";

export async function getWorkoutExercises(workout_id) {
    const response = await axios.get(`exercises/${workout_id}/exercises`);
    return response.data;
}