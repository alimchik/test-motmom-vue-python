<template>
  <div id="app">
    <portal-target name="modal-window"></portal-target>
    <TheNavbar />
    <router-view></router-view>
  </div>
</template>

<script>
import TheNavbar from './components/layout/TheNavbar'
import 'vue-toast-notification/dist/theme-sugar.css'

export default {
  components: {
    TheNavbar
  }
}
</script>
