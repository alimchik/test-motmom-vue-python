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
          localStorage.setItem('token', result.data.token)
          commit('authSuccess', token, user)
        }
      } catch (e) {
        throw new Error(e.response.data.message)
      }
    },

    async refreshJWT ({ commit }) {
      const token = localStorage.getItem('token')
      const beginIndex = token.indexOf('.') + 1
      const endIndex = token.indexOf('.', beginIndex)
      const publicKey = token.substring(beginIndex, endIndex)
      const expDate = JSON.parse(atob(publicKey)).exp * 1000

      const howMuchToRefresh = new Date((new Date(expDate)).getTime() - 1000 * 60)
      const currentTime = new Date()
      const dif = howMuchToRefresh - currentTime

      try {
        if (dif > 0) {
          await setTimeout(async () => {
            const result = await myAxios.get('auth/refresh')
            localStorage.setItem('token', result.data.token)
            commit('refreshToken', result.data.token)
          }, dif)
        }
      } catch (e) {
        console.log(e)
      }
    }
  }
}
