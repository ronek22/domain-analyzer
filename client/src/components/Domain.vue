<template>
  <div>
    <v-content>
      <v-container fluid>
        <v-data-table
          :headers="headers"
          :items="domains"
          class="elevation-1"
          :pagination.sync="pagination"
          :total-items="totalItems"
          :rows-per-page-items="[5,10,25,50]"
        >
          <template v-slot:items="props">
            <td
              @onclick="test"
              v-for="col in headers"
              :key="col.value"
              class="text-xs-right"
              v-html="status_format(props.item[col.value], col.text)"
            ></td>
          </template>
        </v-data-table>
      </v-container>
    </v-content>
    <FileUpload />
  </div>
</template>

<script>
import axios from "axios";
import FileUpload from "./FileUpload.vue";

export default {
  name: "Domain",
  data() {
    return {
      headers: [
        { text: "Id", value: "id", align: "left", sortable: true },
        { text: "Domain", value: "name" },
        { text: "Registartion Date", value: "registration_date" },
        { text: "Expiration Date", value: "expiration_date" },
        { text: "Checked?", value: "checked", sortable: false }
      ],
      domains: [],
      totalItems: 0,
      pagination: {
        page: 1,
        rowsPerPage: 10
      },
      msg: ""
    };
  },
  components: {
    FileUpload
  },
  watch: {
    pagination: {
      async handler() {
        const path = "http://localhost:5000/domains";
        const rowsPerPage = this.pagination.rowsPerPage;
        const pageNumber = this.pagination.page;
        const sortBy = this.pagination.sortBy;
        const descending = this.pagination.descending;
        const config = {
          rows: rowsPerPage,
          page: pageNumber,
          sortBy: sortBy,
          desc: descending
        };

        axios
          .get(
            path +
              `?rows=${rowsPerPage}&page=${pageNumber}&sort=${sortBy}&desc=${descending}`
          )
          .then(res => {
            this.domains = res.data.domains;
            this.totalItems = res.data.total;
          });
        console.log(config);
      },
    }
  },
  methods: {
    test() {
      console.log(pagination);
    },
    status_format(para, name) {
      let status_html = "";
      if (name.includes("Date")) {
        if (!para) return para;
        var newDate = new Date();
        newDate.setTime(para * 1000);
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

    // getDomains() {
    //   const path = "http://localhost:5000/domains";
    //   axios
    //     .get(path)
    //     .then(res => {
    //       this.domains = res.data.domains;
    //     })
    //     .catch(error => {
    //       // eslint-disable-next-line
    //       console.error(error);
    //     });
    // }
  },

  // created() {
  //   this.getDomains();
  // }
};
</script>
