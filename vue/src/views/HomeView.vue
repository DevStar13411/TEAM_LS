<template>
  <div class="home">
    <img alt="logo" src="../assets/logo_small.png">
    <h1>Welcome to ZzangBaguni</h1>
    <div style="margin-top: 15px">
      <AddressSearch/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import AddressSearch from '@/components/Address.vue';

export default {
  name: 'HomeView',
  components: {
    AddressSearch
  }
};
</script>
