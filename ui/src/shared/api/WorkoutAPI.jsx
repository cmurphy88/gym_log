import { axios } from "../../libs/axios";

export async function getUsersWorkouts(user_id) {
    const response = await axios.get(`workouts/user/${user_id}`);
    return response.data;
};

export async function createNewWorkout(name, user_id) {
    const response = axios.post('/workouts/new', {
        name: name,
        user_id: user_id
    });
    console.log(response.Promise);
    return response;
}
