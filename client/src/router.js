import Vue from 'vue';
import Router from 'vue-router';
import Domain from './components/Domain.vue';
import Task from './components/Task.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/domains',
      name: 'Domain',
      component: Domain,
      alias: '/'
    },
    {
      path: '/tasks',
      name: 'Task',
      component: Task,
    },
  ],
});
