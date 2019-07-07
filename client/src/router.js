import Vue from 'vue';
import Router from 'vue-router';
import Domain from './components/Domain.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/domains',
      name: 'Domain',
      component: Domain,
    },
  ],
});
