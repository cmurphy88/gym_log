import { axios } from "../../libs/axios";

export async function getUsersWorkouts(user_id) {
    const response = await axios.get(`workouts/user/${user_id}`);
    return response.data;
};
