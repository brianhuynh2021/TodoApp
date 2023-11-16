import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

const routes = [
    {
      path: '/api', // Client-side URL path
      name: 'CreateTask',
      component: App
    },
    // ... other routes
  ];
  
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  });
  
  export default router;