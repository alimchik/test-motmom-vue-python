<template>
  <AuthForm @go-to-page='goToPage'/>
</template>

<script>
import AuthForm from '@/components/AuthForm'

export default {
  components: {
    AuthForm
  },

  methods: {
    goToPage: function () {
      this.$router.push('/products')
    }
  }
}
</script>
