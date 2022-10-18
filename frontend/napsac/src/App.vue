<template>
  <div v-if="LoginView" class="login_container">
    <Login></Login>
    <AppButton></AppButton>
  </div>
  <template v-else>
    <div class="signup_container">
      <SignUp></SignUp>
      <AppButton></AppButton>
    </div>

  </template>
</template>

<script>

import AppButton from './components/AppButton.vue';
import Login from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      LoginView: true


    }
  },
  components: {
    AppButton,
    Login,
    SignUp

  },
  method: {

  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Solway:wght@300&display=swap');

#app {
  font-family: 'Solway', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.login_container,
.signup_container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: auto;
  flex-direction: column;
}
</style>
