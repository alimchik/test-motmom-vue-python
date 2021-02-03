<template>
  <header class="header-navbar bg-white ">
    <div class="container-fluid pr-3 pl-3 pr-sm-5 pl-sm-5">
      <div class="row">
        <div class="col d-flex justify-content-end">
          <my-button :classes="['btn', 'btn-primary', 'btn-lg']" name="Выйти" v-if="isLoggedIn" :click="logout"/>
          <div class="d-flex justify-content-end" v-else>
            <my-link
              :classes="['btn', 'btn-primary', 'btn-lg','mr-3']"
              component='login'
            >
              Войти
            </my-link>
            <my-link
              :classes="['btn', 'btn-primary', 'btn-lg']"
              component='registration'
            >
              Регистрация
            </my-link>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import Link from '../common/Link'
import Button from '../common/Button'

export default {
  computed: {
    isLoggedIn () {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout: function () {
      this.$store.commit('logout')
      this.$router.push('/login')
    }
  },
  components: {
    'my-link': Link,
    'my-button': Button
  }
}
</script>

<style lang="scss">

.header-navbar {
  height: 80px;
  display: flex;
  align-items: center;
}
</style>
