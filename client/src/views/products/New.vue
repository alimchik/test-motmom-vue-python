<template>
  <ProductForm
    @go-to-page='goToPage'
    title='Добавить'
  />
</template>

<script>
import ProductForm from '../../components/products/ProductForm'

export default {

  components: {
    ProductForm
  },

  methods: {
    goToPage: function () {
      this.$router.push('/products')
    }
  }
}
</script>
