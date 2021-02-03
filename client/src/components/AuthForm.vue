<template>
  <div class="container">
    <div class="row justify-content-center mt-5">
      <div class="col-11 col-lg-8 p-3 p-sm-5 shadow">
        <h2 v-if="getUrl === 'login'" class="h3 mb-3 text-center">Войти</h2>
        <h2 v-else class="h3 mb-3 text-center">Регистрация</h2>
        <form class="bg-white p-3 border rounded" @submit.prevent="submitHandler">
          <FieldForm
            type="email"
            title="Email"
            name="email"
            placeholder="Введите ваш email"
            v-bind:field.sync="email"
          />
          <FieldForm
            type="password"
            title="Пароль"
            name="password"
            placeholder="Введите ваш пароль"
            v-bind:field.sync="password"
          />
          <Button v-if="getUrl === 'login'" :click="submitHandler" :classes="['btn', 'btn-outline-success', 'btn-lg', 'btn-block']" name="Войти"/>
          <Button v-else :click="submitHandler" :classes="['btn', 'btn-outline-success', 'btn-lg', 'btn-block']" name="Регистрация"/>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import FieldForm from './common/FieldForm'
import Button from './common/Button'

export default {
  computed: {
    getUrl: function () {
      return this.$route.path.substring(1, this.$route.path.length)
    }
  },

  data () {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    // submitHandler: function () {
    //   const email = this.email
    //   const password = this.password

    //   // Вход в систему
    //   if (this.getUrl === 'login') {
    //     this.$store.dispatch('login', { email, password })
    //       .then((data) => {
    //         this.$emit('go-to-page')
    //       })
    //       .catch(err => this.$toast.error(err.message))
    //     return
    //   }
    //   // Регистрация
    //   this.$store.dispatch('registr', { email, password })
    //     .then((data) => {
    //       this.$toast.success(data)
    //       this.$emit('go-to-page')
    //     })
    //     .catch(err => this.$toast.error(err.message))
    // },
    submitHandler: async function () {
      const email = this.email
      const password = this.password
      try {
        // Вход в систему
        if (this.getUrl === 'login') {
          await this.$store.dispatch('login', { email, password })
          this.$emit('go-to-page')
          return
        }
        // Регистрация
        await this.$store.dispatch('registr', { email, password })
          .then((data) => {
            this.$toast.success(data)
            this.$emit('go-to-page')
          })
      } catch (e) {
        this.$toast.error(e.message)
      }
    }
  },

  components: {
    FieldForm,
    Button
  }
}
</script>
