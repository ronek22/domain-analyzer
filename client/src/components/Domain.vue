<template>
  <div>
    <v-data-table :headers="headers" :items="domains" :items-per-page="5" class="elevation-1">
      <template v-slot:items="props">
        <td
          v-for="col in headers"
          :key="col.value"
          class="text-xs-right"
          v-html="status_format(props.item[col.value], col.text)"
        ></td>
      </template>
    </v-data-table>
    <FileUpload />
  </div>
</template>

<script>
import axios from "axios";
import FileUpload from "./FileUpload.vue";
import moment from 'moment'

export default {
  name: "Domain",
  data() {
    return {
      headers: [
        { text: "Id", value: "id", align: "left", sortable: true },
        { text: "Domain", value: "name" },
        { text: "Registartion Date", value: "registration_date" },
        { text: "Expiration Date", value: "expiration_date" },
        { text: "Checked?", value: "checked", sortable: false },

      ],
      domains: [],
      msg: ""
    };
  },
  components: {
    FileUpload
  },
  methods: {

    status_format(para, name) {
      let status_html = "";
      if(name.includes('Date')) {
        if(!para)
          return para;
        var newDate = new Date();
        newDate.setTime(para*1000);
        return newDate.toUTCString();
      }
      switch (para) {
        case false:
          status_html =
            '<i title="failed" class="material-icons icon red--text">error</i>';
          break;
        case true:
          status_html =
            '<i title="finished" class="material-icons icon green--text">check_circle</i>';
          break;
        default:
          return para;
      }
      return status_html;
    },

    getDomains() {
      const path = "http://localhost:5000/domains";
      axios
        .get(path)
        .then(res => {
          this.domains = res.data.domains;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },

  created() {
    this.getDomains();
  },

};
</script>
