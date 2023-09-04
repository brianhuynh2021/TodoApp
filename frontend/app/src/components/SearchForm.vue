<template>
  <div class="search-button">
    <input type="text" placeholder="Search a task..." v-model="searchQuery" @keyup.enter="searchTask">
    <button @click="searchTask">Search</button>
  </div>
</template>

<script>
export default {
  data() {
    return {searchQuery: ''}
  },
  methods: {
    searchTask() {
      this.$emit('search', this.searchQuery)
      this.searchQuery = ''
    }
  }
}
</script>

<style scoped>

.search-button {
    margin-bottom: 18px;
}
button:hover {
  background: rgb(255, 174, 0);
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