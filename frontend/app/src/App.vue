<template>
  <div class="todo-app" id="todo-app">
    <h1 id="todo-list-title">Todo List</h1>
    <SearchForm />
    <div id="add-task-div">
      <input placeholder="Add a new task" v-model="newTask" @keyup.enter="addTask">
      <button id="add-task-button" @click="addTask">Add</button>
    </div>

    <div id="task-list-div">
      <ul>
        <li v-for="(task, index) in tasks" :key="index">
          <input type="checkbox" v-model="task.completed">
          <span v-if="task.completed" style="text-decoration: line-through;">{{ task.text }}</span>
          <span v-else> {{ task.text }}</span>
        </li>
     </ul>
    </div>

  </div>
</template>


<script>
import SearchForm from './components/SearchForm.vue'

export default {
  components: {
    SearchForm
  },
  data() {
    return {
      newTask: '',
      tasks: [],
    };
  },
  computed: {
  },
  methods: {
    addTask() {
      if (this.newTask && this.newTask !== ''){
        this.tasks.push({
          text: this.newTask,
          completed: false
        })
        this.newTask = ''
      }
  }
  },
};
</script>


<style>
#todo-list-title{
  color:rgb(255, 98, 0);
}
.todo-app {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
  font-size: 17px;
}

#add-task-div{
  width: 25%;
  height: auto;
  position: relative;
  display: flex;
  justify-content: right;
  margin: 0 auto;
  margin-bottom: 15px;
}

#add-task-div input{
  width: 184px;
  font-size: 17px;
}
#add-task-div button {
  background-color: #59e73c;
  color: white;
  box-sizing: content-box;
  border: 1px solid grey;
  width: 53px;
  height: 20px;
  cursor: pointer;
  margin-right: 86px;
  font-size: 17px;
}

#add-task-button:hover {
  background-color: orangered;
}

#task-list-div {
  border-radius: 5px;
  background: rgb(240, 230, 230);
  background-position: left top;
  background-repeat: repeat;
  padding: 20px;
  width: 400px;
  height: auto;
  margin: 0 auto;
}

ul {
  list-style: none;
  text-align: left;
}
</style>
