<template>
  <div class="form-row">
    <div class="col">
      <div class="form-group">
        <label :for="name">{{title}}</label>
        <input
          :type="type"
          :id="name"
          class="form-control"
          required
          :placeholder="placeholder"
          :value="value"
          @input="inputHandler($event)"
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      required: true,
      validator: function (value) {
        return ['email', 'password', 'text', 'date'].indexOf(value) !== -1
      }
    },
    name: {
      type: String,
      required: true,
      validator: function (value) {
        return ['email', 'password', 'name-product', 'count', 'price', 'date_add'].indexOf(value) !== -1
      }
    },
    placeholder: {
      type: String,
      default: function () {
        return ''
      }
    },
    title: {
      type: String,
      required: true
    },
    value: {
      type: [String, Number]
    }
  },

  methods: {
    inputHandler: function (event) {
      this.$emit('update:field', event.target.value)
    }
  }
}
</script>
