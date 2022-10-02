<template>

  <AppLogin></AppLogin>
</template>

<script>
import AppLogin from './components/AppLogIn.vue';


export default {
  name: 'App',
  components: {
    AppLogin,

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
