<template>
  <v-app>
    <v-toolbar dark app>
      <v-toolbar-title>Menadżer domen</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn flat to="/domains" exact>Domeny</v-btn>
        <v-btn flat to="/tasks" exact>Zadania</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <!-- <v-tabs fixed-tabs>
      <v-tab to="/domains">Domains</v-tab>
      <v-tab to="/tasks">Tasks</v-tab>
    </v-tabs> -->
    <router-view></router-view>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>
