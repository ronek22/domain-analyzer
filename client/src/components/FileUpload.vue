<template>
  <div>
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
      const path = 'http://localhost:5000/domains';
      let formData = new FormData();
      formData.append('file', this.file);
      axios.post(path, formData)
        .then(res => console.log("SUCCESS"))
        .catch(err => console.error(err));

    }
  }
  // methods: {
  //   onFileChange(e) {
  //     e.preventDefault();
  //     const files = e.target.files || e.dataTransfer.files;
  //     if (!files.length) return;
  //     this.createFile(files[0]);
  //     console.log("FILE:", files[0]);
  //   },
  //   createFile(file) {
  //     const reader = new FileReader();
  //     const vm = this;
  //     reader.onload = e => {
  //       vm.file = e.target.result;
  //     };
  //     reader.readAsDataURL(file);
  //   },
  //   upload() {
  //     const path = "http://localhost:5000/domains";
  //     const data = new FormData();
  //     data.append("file", document.getElementById("file").files[0]);
  //     axios
  //       .post(path, data)
  //       .then(res => console.log(res))
  //       .catch(err => {
  //         console.error(err);
  //       });
  //   }
  // }
};
</script>
