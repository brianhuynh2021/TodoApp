<template>
  <div class="todo-app" id="todo-app">
    <h1 id="todo-list-title">Todo List</h1>
    
    <div id="add-task-to-list">
      <SearchForm @search="handleSearch"/>
      <input placeholder="A new task" v-model="newTask" @keyup.enter="addTask">
      <button id="add-task-button" @click="addTask">Add</button>
    </div>
    <!-- All tasks button -->
    <div><button id="all-task-btn" @click="loadAllTasks">All tasks</button></div>
    <!-- End all tasks button -->
    <div v-if="filteredTasks.length > 0"  id="task-list-div">
      <ul v-for="(task, index) in filteredTasks" :key="index">
        <li @dblclick="toggleEdit(task)">
          <input type="checkbox" v-model="task.completed" @change="updateTime(task)">
          <span v-if="!task.editing" :class="{'task-completed': task.completed}">
            {{ task.newTask }} - {{ task.timeAdded }}
          </span>
          <input
            v-else
            v-model="task.newTask"
            @keyup.enter="saveEdit(task)"
            @blur="saveEdit(task)"
          >
          <button class="delete-button" @click="deleteTask(index)">Del</button>
        </li>
      </ul>
    </div>
    <div v-else class="no-tasks">
          <span>No tasks added yet...</span>
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
      filteredTasks: [],
    };
  },
  created() {
      this.filteredTasks = this.tasks
    },
  methods: {
    addTask() {
      if (this.newTask && this.newTask.trim() !== '') {
        // Construct the data to send in the request
        const taskData = {
          task_name: this.newTask // Ensure this matches the expected field in your Django API
        };

        // Make a POST request to the server
        fetch(`${process.env.baseURL}/api/todos/new_task/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // 'Authorization': 'Token your_token_here' // Uncomment if you need to send a token
          },
          body: JSON.stringify(taskData)
        })
        .then(response => response.json())
        .then(data => {
          // If the request was successful, push the new task to the tasks array
          this.tasks.push({
            id: data.id,
            task: data.task,
            completed: data.completed,
            created_at: data.created_at,
            completed_at: data.completed_at,
            editing: false, // Assuming you want to control editing state on the frontend
          });
          this.newTask = ''; // Reset the newTask input
          this.filteredTasks = [...this.tasks]; // Update any filtered views you have
        })
        .catch(error => {
          console.error("There was an error creating the task:", error);
        });
      }
    },
    getTimeAdded() {
      const now = new Date()
      const hours = String(now.getHours()).padStart(2, '0')
      const minutes = String(now.getMinutes()).padStart(2, '0')
      const seconds = String(now.getSeconds()).padStart(2, '0')
      const day = String(now.getDate()).padStart(2, '0')
      const month = String(now.getMonth() + 1).padStart(2, '0')
      const year = now.getFullYear()
      
      return `${hours}:${minutes}:${seconds} ${day}/${month}/${year}`
    },
    updateTime(task) {
      task.timeAdded = this.getTimeAdded()
    },
    toggleEdit(task) {
      if (!task.editing) {
        task.lastEdited = task.newTask
      }
      task.editing = !task.editing
    },
    saveEdit(task) {
      task.editing = false
      if (task.newTask.trim() !== '' && task.newTask !== task.lastEdited) {
        task.lastEdited = ''
        task.timeAdded = this.getTimeAdded()
      } else {
        task.newTask = task.lastEdited
      }
    },
    handleSearch(query) {
    if (query) {
        this.filteredTasks = this.tasks.filter(task => task.newTask.toLowerCase().includes(query.toLowerCase()));
      } else {
        this.filteredTasks = [...this.tasks]
      }
    },
    deleteTask(index) {
      if (window.confirm("Are you sure you want to delete this task?")) {
        this.tasks.splice(index, 1);
        this.filteredTasks = [...this.tasks]
      }
    },
    loadAllTasks() {
      this.filteredTasks = [...this.tasks]
    },
  }
}
</script>


<style>
@import './styles.css';

#todo-list-title{
  color:rgb(255, 98, 0);
  position: relative;
  left: -40px;
}
.todo-app {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
  font-size: 17px;
  height: 1200px;
  width: 1200px;
}

#add-task-to-list{
  width: 50%;
  height: auto;
  position: relative;
  left: 250px;
  margin-bottom: 15px;
  border-bottom: 1px solid grey;
  padding-bottom: 15px;
}

#add-task-to-list input{
  width: 183.5px;
  font-size: 17px;
}
#add-task-button {
  background-color: #59e73c;
  color: white;
  box-sizing: content-box;
  border: 1px solid grey;
  width: 53px;
  height: 20px;
  cursor: pointer;
  font-size: 17px;
}

#add-task-button:hover {
  background-color: rgb(255, 174, 0);
}

#task-list-div {
  border-radius: 5px;
  background: rgb(240, 230, 230);
  background-position: left top;
  background-repeat: repeat;
  padding: 0.5px;
  width: 400px;
  height: auto;
  margin-left: 600px;
  margin-top: 10px;
  display: block;
}

ul {
  list-style: none;
  text-align: left;
  
}

.task-completed {
  text-decoration: line-through;
}


li {
  height: 40px;
  line-height: 18px;
}

.delete-button {
  background-color: rgb(255, 98, 0);
  color: white;
  border: none;
  cursor: pointer;
  height: 40%; 
  width: 30px;
  line-height: inherit;
  margin-top: 2px;
  display: inline-block;
  margin-left: 5px;
  text-align: top;
  filter: blur(1px);
  position: relative;
  visibility: hidden;
}

.delete-button:hover {
  background-color: red;
  filter: none;
}

li:hover .delete-button {
  visibility: visible
}

#all-task-btn {
  background-color: rgb(255, 174, 0);
  color: rgb(255, 255, 255);
  margin-right: 0 auto;
  position: relative;
  left: -60px;
  margin-bottom: 20px;
}

#all-task-btn:hover {
  background-color: #59e73c;
  color: rgb(241, 232, 242);
}

.no-tasks {
  border: 1px solid #ccc;
  width: 20%;
  padding: 20px;
  text-align: center;
  background-color: #f9f9f9;
  color: rgb(255, 98, 0);
  margin: 0 auto;
  position: relative;
  left: -52px;
}

li {
  height: 40px;
  line-height: 18px;
  margin: -10px;
  padding: 0;
}
</style>