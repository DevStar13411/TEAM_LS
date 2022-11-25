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
          </ul>        
        </div>
      </div>   
    </nav>
  </header>
  <main>
    <div class="content">
      <video autoplay="autoplay" loop="loop" muted="muted">
        <source src="../assets/grocery.mp4" type="video/mp4">
      </video>
      <div class="home">
          <!-- <img alt="logo" src="../assets/logo_small.png"> -->
          <h1 class="text-white fw-bold">Welcome to ZzangBaguni</h1>
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

<style>
.home {
  position: absolute;
  left: 0;
  bottom: 8%;
  width: 100%;
}
.content {
  position: relative;
  width: 100%;
  margin: 0 auto;
}
.content video {
  width: 100%;
  display: block;
}
.content:before {
  content: '';
  position: absolute;
  background: rgba(0, 0, 0, 0.5);
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>