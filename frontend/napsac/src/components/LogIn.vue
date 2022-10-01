<template>
    <div class="login">
        <label for="username"> Username </label>
        <input type="text" id="username">
        <label for="password"> Password</label>
        <input type="text" id="password">

        <button> Log in </button>
    </div>
</template>

<style>
.login {
    display: flex;
    position: relative;
    width: auto;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    top: 100px;

}

label {
    font-size: 25px;
}

#username {
    width: 350px;
    height: 50px;
    align-self: center;
    border-radius: 15px;
}

#password {
    width: 350px;
    height: 50px;
    align-self: center;
    border-radius: 15px;
}

button {
    background-color: #2F88FF;
    width: 300px;
    height: 50px;
    align-self: center;
    margin: 50px;
    border-radius: 15px;
    color: white;
    font-size: 20px;
}
</style>