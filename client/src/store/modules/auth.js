import { myAxios } from '@/api/http-common'

export default {
  state: {
    status: '',
    user: {},
    token: localStorage.getItem('token') || ''
  },

  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status
  },

  mutations: {
    authRequest (state) {
      state.status = 'loading'
    },
    authSuccess (state, token, user) {
      state.status = 'success'
      state.token = token
      state.user = user
    },
    logout (state) {
      state.status = ''
      state.token = ''
      state.user = { ...{} }
      localStorage.removeItem('token')
    },
    refreshToken (state, token) {
      state.token = token
    }
  },
  actions: {
    async registr ({ commit }, user) {
      try {
        const result = await myAxios.post('auth/registr', user)
        if (result.status === 201) {
          return Promise.resolve(result.data.message)
        }
      } catch (e) {
        throw new Error(e.response.data.message)
      }
    },
    async login ({ commit }, user) {
      commit('authRequest')
      try {
        const result = await myAxios.post('auth/login', user)
        if (result.status === 200) {
          const token = result.data.token
          const user = result.data.user
          myAxios.defaults.headers.Autorization = result.data.token
          localStorage.setItem('token', result.data.token)
          commit('authSuccess', token, user)
        }
      } catch (e) {
        throw new Error(e.response.data.message)
      }
    },

    refreshJWT ({ commit }) {
      let token = localStorage.getItem('token')
      let beginIndex = token.indexOf('.') + 1
      let endIndex = token.indexOf('.', beginIndex)
      let publicKey = token.substring(beginIndex, endIndex)
      let expDate = JSON.parse(atob(publicKey)).exp * 1000

      let howMuchToRefresh = new Date((new Date(expDate)).getTime() - 1000 * 10)
      let currentTime = new Date()
      let dif = howMuchToRefresh - currentTime
      let entry = 0

      const refresh = async function () {
        if (entry !== 0) {
          try {
            if (dif > 0) {
              const result = await myAxios.get('auth/refresh')
              token = result.data.token
              beginIndex = token.indexOf('.') + 1
              endIndex = token.indexOf('.', beginIndex)
              publicKey = token.substring(beginIndex, endIndex)
              expDate = JSON.parse(atob(publicKey)).exp * 1000
              howMuchToRefresh = new Date((new Date(expDate)).getTime() - 1000 * 10)
              currentTime = new Date()
              dif = howMuchToRefresh - currentTime
              myAxios.defaults.headers.Autorization = token
              localStorage.setItem('token', token)
              commit('refreshToken', token)
            }
          } catch (e) {
            console.log(e)
          }
        }
        entry += 1
        setTimeout(refresh, dif)
      }
      refresh()
    }
  }
}
