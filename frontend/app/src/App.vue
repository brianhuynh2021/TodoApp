<template>
  <div class="todo-app">
    <h1>To-Do List App</h1>
    <input v-model="newTask" @keyup.enter="addTask" placeholder="Add a new task">
    <ul class="task-list">
      <li v-for="(task, index) in tasks" :key="index" class="task-item">
        <input type="checkbox" v-model="task.completed" @change="toggleCompleted(index)" class="task-checkbox">
        <span v-if="!task.editing">{{ task.text }}</span>
        <input v-else v-model="task.updatedText" @keyup.enter="saveTask(index)" class="edit-input">
        <button @click="toggleEdit(index)" class="edit-button">{{ task.editing ? 'Save' : 'Edit' }}</button>
        <button @click="deleteTask(index)" class="delete-button">Delete</button>
        <span class="task-timestamp">Created: {{ formatDate(task.creationTime) }}</span>
        <span v-if="task.completed" class="task-timestamp">Completed: {{ formatDate(task.completionTime) }}</span>
      </li>
    </ul>
    <div v-if="completedTasks.length > 0" class="completed-tasks">
      <h2>Completed Tasks</h2>
      <ul>
        <li v-for="(task, index) in completedTasks" :key="index">{{ task.text }}</li>
      </ul>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      newTask: '',
      tasks: [],
    };
  },
  computed: {
    completedTasks() {
      return this.tasks.filter(task => task.completed);
    },
  },
  methods: {
    addTask() {
      if (this.newTask.trim() === '') return;
      this.tasks.push({
        text: this.newTask,
        completed: false,
        editing: false,
        updatedText: '',
        creationTime: new Date(), // Add creation timestamp here
        completionTime: null, // Initialize completion timestamp as null
      });
      this.newTask = '';
    },
    deleteTask(index) {
      this.tasks.splice(index, 1);
    },
    toggleEdit(index) {
      this.tasks[index].editing = !this.tasks[index].editing;
      this.tasks[index].updatedText = this.tasks[index].text;
    },
    saveTask(index) {
      if (this.tasks[index].updatedText.trim() === '') return;
      this.tasks[index].text = this.tasks[index].updatedText;
      this.tasks[index].editing = false;
    },
    toggleCompleted(index) {
      if (this.tasks[index].completed) {
        this.tasks[index].completionTime = new Date(); // Set completion timestamp
      } else {
        this.tasks[index].completionTime = null; // Clear completion timestamp
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric' };
      return new Intl.DateTimeFormat('en-US', options).format(date);
    },
  },
};
</script>



<style>
.todo-app {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

.task-list {
  list-style: none;
  padding: 0;
}

.task-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.task-checkbox {
  margin-right: 10px;
}

.delete-button {
  background-color: #e74c3c;
  border: none;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 14px;
}


.edit-input {
  width: 80%;
  padding: 4px;
  margin-right: 10px;
}

.edit-button {
  background-color: #3498db;
  border: none;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 14px;
  margin-right: 5px;
}

/* Additional styles for the editing mode */
.task-item {
  position: relative;
}

.edit-button {
  position: absolute;
  right: 80px;
  }
  .completed-tasks {
  margin-top: 20px;
  padding-top: 10px;
  border-top: 1px solid #ddd;
}

.completed-tasks h2 {
  margin-bottom: 10px;
}

.completed-tasks ul {
  list-style: disc;
  padding-left: 20px;
}
.task-timestamp {
  color: #888;
  font-size: 12px;
  display: block;
  margin-top: 4px;
}
</style>
