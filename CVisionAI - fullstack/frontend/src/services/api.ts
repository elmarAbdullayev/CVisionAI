import axios from "axios"


const BASE_URL = "http://127.0.0.1:8000/api/analyze"


export const postData = async (data: FormData) => {
    const response = await axios.post(BASE_URL,data);
    return response.data;
};