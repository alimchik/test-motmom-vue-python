import { myAxios } from '@/api/http-common'
import formatData from '../../helpers/formatData.js'

export default {
  state: {
    products: [],
    product: {}
  },
  getters: {
    allProducts (state) {
      return state.products.map(item => {
        return { ...item, date_add: formatData(item.date_add, 'dd.mm.yyyy') }
      })
    },
    product (state) {
      return { ...state.product, date_add: formatData(state.product.date_add, 'yyyy-mm-dd') }
    },
    isSomeItemSelected (state) {
      return state.products.some(item => item.selected === true)
    }
  },
  mutations: {
    insertProducts (state, result) {
      const result2 = result.map(item => {
        item.selected = false
        return item
      })

      state.products = result2
    },

    insertProduct (state, product) {
      state.product = product
    },

    updateCheckProduct (state, id) {
      const result = state.products.map(item => {
        if (item.id === id) {
          return { ...item, selected: !item.selected }
        }
        return item
      })

      state.products = [...result]
    },

    updateAllCheckProduct (state, check) {
      const result = state.products.map(item => {
        return { ...item, selected: check }
      })
      state.products = [...result]
    },

    updateProduct (state, product) {
      state.products = [...state.products.filter(item => item.id !== product.id), product]
    }
  },
  actions: {
    async getProducts ({ commit }, param = '') {
      let result = []
      const qweryParams = param ? `?name=${param}` : ''
      const url = `products${qweryParams}`
      try {
        result = await myAxios.get(url)
      } catch (e) {
        console.log('статут', e.response.data.title)
        if (e.response.status === 403) {
          throw new Error(e.response.data.title)
        }
        throw new Error(e.response.data.message)
      }
      commit('insertProducts', result.data)
    },

    async getProduct ({ commit }, id) {
      let result = []
      try {
        result = await myAxios.get(`products/${id}`)
      } catch (e) {
        throw new Error(e.response.data.message)
      }
      commit('insertProduct', result.data)
    },

    async removeProduct ({ dispatch }, ids) {
      let result = []
      try {
        result = await myAxios({
          method: 'DELETE',
          url: 'products',
          data: {
            data: ids
          }
        })
      } catch (e) {
        throw new Error(e.response.data.message)
      }

      if (result.status === 200) {
        await dispatch('getProducts')
        return Promise.resolve(result.data.message)
      }
    },

    async removeProductsMulti ({ dispatch, state }) {
      const arrIds = state.products.filter(item => item.selected).map(item => item.id)
      await dispatch('removeProduct', arrIds)
    },

    async addProduct ({ commit, dispatch }, product) {
      let status = null
      let result = []
      try {
        result = await myAxios.post('products', product)
        status = result.status
      } catch (e) {
        throw new Error(e.response.data.message)
      }

      if (status === 201) {
        await dispatch('getProducts')
        return Promise.resolve(result.data.message)
      }
    },

    async editProduct ({ commit }, product) {
      let result = []
      try {
        result = await myAxios.patch(`products/${product.id}`, product)
      } catch (e) {
        throw new Error(e.response.data.message)
      }
      commit('updateProduct', result.data)
      return Promise.resolve('Данные успешно обновленны')
    }
  }
}
