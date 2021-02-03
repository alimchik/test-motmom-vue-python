import axios from 'axios'

export const myAxios = axios.create({
  baseURL: 'http://localhost:8060/api/',
  headers: {
    Autorization: localStorage.getItem('token')
  }
})
