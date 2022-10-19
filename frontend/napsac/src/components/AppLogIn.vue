<template>˜
    <div class="login">
        <label for="username"> Username </label>
        <input type="text" id="username">
        <label for="password"> Password</label>
        <input type="text" id="password">
        <p> Don't have an account? <a href="#"> Sign up</a></p>

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
    width: 300px;
    height: 40px;
    align-self: center;
    border-radius: 10px;
    border-color: black;
    border-style: solid;
    border-width: 1px;
    margin: 10px;
}

#password {
    width: 300px;
    height: 40px;
    align-self: center;
    border-radius: 10px;
    border-color: black;
    border-style: solid;
    border-width: 1px;
    margin: 5px;
}

button {
    background-color: #2F88FF;
    width: 300px;
    height: 45px;
    align-self: center;
    margin: 40px;
    border-radius: 10px;
    border-color: black;
    border-style: solid;
    border-width: 1px;
    color: white;
    font-size: 20px;
}

p {
    margin: 5px;
    position: relative;
    right: -33px;

}
</style>
<script>

</script>