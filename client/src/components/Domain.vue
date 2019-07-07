<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Domain",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/domains";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>