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
  </div>
</template>

<script>
import axios from "axios";



export default {
  name: "FileUpload",
  data() {
    return {
      file: null
    };
  },
  methods: {

    onSubmit() {
      const path = "http://localhost:5000/domains";
      const formData = new FormData();
      formData.append("file", this.file);
      axios
        .post(path, formData)
        .then(console.log("SUCCESS"))
        .catch(err => console.error(err));
    }
  }
};
</script>
