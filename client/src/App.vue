<template>
  <v-app>
    <v-tabs fixed-tabs>
      <v-tab to="/domains">Domains</v-tab>
    </v-tabs>
    <router-view></router-view>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>
