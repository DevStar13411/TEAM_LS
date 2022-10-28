<template>
  <div class="home">
    <img alt="logo" src="../assets/logo_small.png">
    <HelloWorld msg="Welcome to ZzangBaguni"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
};
</script>
