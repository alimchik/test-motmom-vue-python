import axios from 'axios'

export const myAxios = axios.create({
  baseURL: 'http://localhost:8061/api/',
  headers: {
    Autorization: localStorage.getItem('token')
  }
})
