<template>
  <div>
    <v-content>
      <v-container fluid>
        <v-data-table
          :headers="headers"
          :items="tasks"
          :items-per-page="5"
          class="elevation-1"
          :loading="loading"
        >
          <template v-slot:items="props">
            <td class="text-xs-left">{{ props.item.id }}</td>
            <td class="text-xs-left">{{ props.item.state }}</td>
            <td class="text-xs-left">{{ props.item.current }} / {{props.item.total}}</td>
            <!-- Maybe add start time -->
          </template>
        </v-data-table>
      </v-container>
    </v-content>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Task",
  data() {
    return {
      headers: [
        { text: "Id", value: "id", align: "left", sortable: true },
        { text: "Status", value: "state" },
        { text: "Stan", value: "current" },
      ],
      tasks: [],
      loading: false,
    };
  },
  mounted() {
    let query = setInterval(this.getTasks, 1000*10);  
  },
  created() {
      this.getTasks();
  },
  methods: {
    getTasks() {
        this.loading = true;
      const path = "http://localhost:5000/status";
      axios.get(path).then(res => {
        this.tasks = res.data.tasks;
        this.loading=false;
      });
    },
  }
};
</script>
