<template>
  <modal-window :click="closeModal" :title="title">
    <form class="bg-white p-3 border rounded m-4" @submit.prevent="submitHandler">
      <FieldForm
        type="text"
        title="Название товара"
        name="name-product"
        placeholder="Введите название товара"
        :value="name"
        v-bind:field.sync="name"
      />
      <FieldForm
        type="text"
        title="Количество товара"
        name="count"
        placeholder="шт."
        :value="count"
        v-bind:field.sync="count"
      />
      <FieldForm
        type="text"
        title="Стоимость товара"
        name="price"
        placeholder="руб."
        :value="price"
        v-bind:field.sync="price"
      />
      <FieldForm
        type="date"
        title="Дата добавления"
        name="date_add"
        :value="date_add"
        v-bind:field.sync="date_add"
      />
      <Button :click="submitHandler" :classes="['btn', 'btn-outline-success', 'btn-lg', 'btn-block']" :name="title"/>
    </form>
  </modal-window>
</template>

<script>
import { mapGetters } from 'vuex'
import FieldForm from '../common/FieldForm'
import Button from '../common/Button'
import ModalWindow from '../common/ModalWindow'

export default {
  data () {
    return {
      name: '',
      count: '',
      price: '',
      date_add: ''
    }
  },

  computed: mapGetters(['product']),

  props: ['title'],

  methods: {
    closeModal: function () {
      this.$emit('go-to-page')
    },

    submitHandler () {
      const product = {
        name: this.name,
        count: this.count,
        price: this.price,
        date_add: this.date_add
      }

      // если изменяем продукт
      if (this.$route.params.id) {
        this.$store.dispatch('editProduct', { ...product, id: this.$route.params.id })
          .then((data) => {
            this.$emit('go-to-page')
            this.$toast.success(data)
          })
          .catch(err => this.$toast.error(err.message))
        return
      }

      // если добавляем продукт
      this.$store.dispatch('addProduct', product)
        .then((data) => {
          this.$emit('go-to-page')
          this.$toast.success(data)
        })
        .catch(err => this.$toast.error(err.message))
    }
  },
  async created () {
    if (!this.$route.params.id) {
      return
    }

    try {
      await this.$store.dispatch('getProduct', this.$route.params.id)
    } catch (e) {
      this.$toast.error(e.message)
    }
    this.name = this.product.name
    this.count = this.product.count
    this.price = this.product.price
    this.date_add = this.product.date_add
  },

  components: {
    FieldForm,
    Button,
    'modal-window': ModalWindow
  }
}
</script>
