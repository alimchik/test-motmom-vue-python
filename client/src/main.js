import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PortalVue from 'portal-vue'
import VueToast from 'vue-toast-notification'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(PortalVue)
Vue.use(VueToast)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
