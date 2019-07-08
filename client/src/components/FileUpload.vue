<template>
  <div class="container">
    <b-form inline @submit.prevent="onSubmit" class="justify-content-center">
      <b-form-file
        accept=".csv, .txt"
        v-model="file"
        :state="Boolean(file)"
        placeholder="Choose a file..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
      <div class="text-center">
        <v-btn outline color="indigo" type="submit" @click="snackbar = true">Upload</v-btn>
      </div>
    </b-form>

    <v-snackbar
      v-model="snackbar"
      :color="color"
      :multi-line="mode === 'multi-line'"
      :timeout="timeout"
      :vertical="mode === 'vertical'"
      class="text-center"
    >
      {{ text }}
      <v-btn dark flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
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
      snackbar: false,
      color: "success",
      mode: "multi-line",
      timeout: 6000,
      text: "Pomyślnie utworzono zadanie"
    };
  },
  methods: {
    onSubmit() {
      const path = "http://51.75.249.84:5000/domains";
      const formData = new FormData();
      formData.append("file", this.file);
      axios
        .post(path, formData)
        .then(res => {
          console.log(res.headers.location);
        })
        .catch(err => console.error(err));
    }
  }
};
</script>


<style scoped>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
