<template>
  <button :class="classes" @click.prevent="click" :disabled="disabled">
    {{ name }}
  </button>
</template>

<script>
export default {
  props: {
    classes: {
      type: Array
    },
    name: {
      type: String,
      required: true
    },
    click: {
      type: Function
    },
    disabled: {
      type: Boolean
    }
  }
}
</script>

<style lang="scss" scoped>
.remove {
  display: block;
  font-weight: 400;
  text-align: center;
  color: #fff;
  background-color: #dc3545;
  border-color: #dc3545;
  opacity: .65;
  border: 1px solid transparent;
  padding: .375rem .75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: .25rem;
  cursor: auto;
  transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
}

.active {
  opacity: 1;
  cursor: pointer;
  &:hover {
    background-color: #c82333;
    border-color: #bd2130;
  }
  &:focus {
    background-color: #c82333;
    border-color: #bd2130;
    box-shadow: 0 0 0 0.2rem rgba(225,83,97,.5);
  }
}
</style>
