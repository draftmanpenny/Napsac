<template>
  <div v-if="LoginView" class="login_container">
    <div class="logo">
      <img src="./assets/napsac.svg" alt="Napsac">
    </div>
    <AppLogin></AppLogin>
  </div>
  <template v-else-if="nav">
    <NavBar></NavBar>
    <RecentBooks></RecentBooks>
  </template>
  <template v-else>
    <div class="signup_container">
      <SignUp></SignUp>
    </div>

  </template>
</template>

<script>

import AppLogin from './components/AppLogIn.vue';
import SignUp from './components/SignUp.vue';
import NavBar from './components/NavBar.vue'
import RecentBooks from './components/RecentBooks.vue';







export default {
  name: 'App',
  data() {
    return {
      LoginView: true,
      nav: true



    }
  },
  components: {
    AppLogin,
    SignUp,
    NavBar,
    RecentBooks,
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
  position: absolute;
  top: 250px;
}

body {

  margin: 0;
}

.logo {
  position: relative;
  left: -875px;
  top: -225px;
}
</style>
