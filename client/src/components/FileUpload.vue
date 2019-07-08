<template>
  <div class="container">
    <b-form inline @submit.prevent="onSubmit">
      <b-form-file
        accept=".csv, .txt"
        v-model="file"
        :state="Boolean(file)"
        placeholder="Choose a file..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
    <!-- <h2>{{ processed }} / {{ total }}</h2> -->
    <!-- <v-progress-linear v-model="progressValue"></v-progress-linear> -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FileUpload",
  data() {
    return {
      file: null,
      progressValue: 0,
      processed: 0,
      total: 1,
    };
  },
  methods: {
    // update_progress(status_url) {
    //     axios.get(status_url).then((res) => {
    //       this.processed = res.data.current;
    //       this.total = res.data.total;
    //       this.progressValue = parseInt(
    //         (res.data.current * 100) / res.data.total
    //       );
    //       if (res.data.state != "SUCCESS" && res.data.state != "FAILURE") {
    //         setTimeout(this.update_progress.bind(null, status_url), 500);
    //       } else {
    //         console.log("SUCCESS");
    //       }
    //     });
    // },
    onSubmit() {
      const path = "http://localhost:5000/domains";
      const formData = new FormData();
      formData.append("file", this.file);
      axios
        .post(path, formData)
        .then((res) => {
          console.log(res.headers.location);
          // this.update_progress(res.headers.location);
        })
        .catch(err => console.error(err));
    }
  }
};
</script>
