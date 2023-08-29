<template>
  <div class="search-button">
    <input type="text" placeholder="Search task...">
    <button>Search</button>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>

.search-button {
    margin-bottom: 20px;
}
button{ 

    background: #2196F3;
    color: white;
    font-size: 17px;
    border: 1px solid grey;
    border-left: none;
    cursor: pointer;
}

input {
    font-size: 17px;
}
</style>