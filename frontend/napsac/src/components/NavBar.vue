<template>
    <div class="nav-container">
        <ul>
            <li> Dashboard</li>
            <li> Connect </li>
            <li> Upload </li>
            <li> Settings </li>
            <li> About us </li>
        </ul>
    </div>
</template>
<style>
.nav-container {
    display: flex;
    border: 1px solid black;
    height: 100vh;
    width: 175px;
    top: 0px;
    position: absolute;


}

ul {
    list-style: none;
    margin-top: 100px;
}

li {
    margin: 15px;
}

li:hover {
    background-color: #FAFF00;

}
</style>