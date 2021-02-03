<template>
  <main>
    <ProductsList @go-to-page='goToPage'/>
    <router-view></router-view>
  </main>
</template>

<script>
import ProductsList from '../../components/products/ProductsList'

export default {
  components: {
    ProductsList
  },
  methods: {
    goToPage: function () {
      this.$router.push('/login')
    }
  }
}
</script>
