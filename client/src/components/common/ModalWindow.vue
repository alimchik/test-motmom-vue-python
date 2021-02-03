<template>
  <portal to="modal-window">
    <div class="modal-background" @click.prevent="click">
    </div>
    <div class="window shadow">
      <div class="header p-4">
        <h2 class="h3">{{ title }}</h2>
        <my-link component='product-list'>
          <i class='fas fa-times'></i>
        </my-link>
      </div>
      <div class="body">
        <slot/>
      </div>
    </div>
  </portal>
</template>

<script>
import Link from '../common/Link'

export default {
  props: {
    title: {
      type: String,
      required: true
    },
    click: {
      type: Function
    }
  },
  components: {
    'my-link': Link
  }
}
</script>

<style lang="scss">
.modal-background {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0,0,0,.3);
  z-index: 10;
}

.window {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  min-height: 200px;
  width: 100%;
  min-width: 320px;
  max-width: 650px;
  box-sizing: border-box;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  z-index: 20;

  .header {
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    align-items: center;

    i {
      color: rgb(0, 0, 0);

      &:hover {
        color: rgb(136, 6, 6);
      }
    }
  }
}

@media screen and (max-width:  650px) {
  .window {
    height: 100vh;
    width: 100%;
  }
}
</style>
