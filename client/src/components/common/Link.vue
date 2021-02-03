<template>
  <router-link :to='{name: component, params: params}' :class="classes">
    <slot/>
  </router-link>
</template>

<script>
export default {
  props: {
    component: {
      type: String,
      required: true
    },
    params: {
      type: Object
    },
    classes: {
      type: Array
    }
  }
}
</script>

<style lang="scss">
.add {
  text-decoration: none;
  display: block;
  font-weight: 400;
  text-align: center;
  color: #fff;
  background-color: #28a745;
  border-color: #28a745;
  border: 1px solid transparent;
  padding: .375rem .75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: .25rem;
  transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;

  &:hover {
    color: #fff;
    text-decoration: none;
    background-color: #218838;
    border-color: #1e7e34;
  }
  &:focus {
    color: #fff;
    text-decoration: none;
    background-color: #218838;
    border-color: #1e7e34;
    box-shadow: 0 0 0 0.2rem rgba(72,180,97,.5);
  }
  &:active {
    color: #fff;
    text-decoration: none;
    background-color: #1e7e34;
    border-color: #1c7430;
  }
}
</style>
