<template>
  <header>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          <img alt="Vue logo" src="@/assets/logo_small.png" style="height:40px;" />
          ZzangBaguni
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
            <li class="nav-item">
              <a href="https://zzangbaguni.shop/map.html" class="nav-link">Map</a>
            </li>
          </ul>        
        </div>
      </div>   
    </nav>
  </header>
  <main>
    <div class="home">
      <img alt="logo" src="../assets/logo_small.png">
      <h1>Welcome to ZzangBaguni</h1>
      <div style="margin-top: 15px">
        <AddressSearch/>
      </div>
    </div>
  </main>
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
