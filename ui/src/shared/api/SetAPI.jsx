import { axios } from "../../libs/axios";

export async function getExerciseSets(exercise_id) {
    const response = await axios.get(`sets/date/${exercise_id}`);
    return response.data;
}