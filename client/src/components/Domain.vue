<template>
  <div class="container">
    <p>{{ msg }}</p>
    <FileUpload />
  </div>
</template>

<script>
import axios from 'axios';
import FileUpload from './FileUpload.vue';

export default {
  name: 'Domain',
  data() {
    return {
      msg: '',
    };
  },
  components: {
    FileUpload,
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/domains';
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
