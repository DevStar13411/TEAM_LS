<template>
    <header>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          <img alt="logo" src="@/assets/logo_small.png" style="height:40px;" />
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
    <section class="showcase" style="position: relative;">
        <div class="video-container">
          <video src="../assets/grocery.mp4" autoplay muted loop></video>
        </div>
        <div class="content">
          <h1 style="color: #fff;">Welcome to ZzangBaguni</h1>
          <AddressSearch/>
          <!-- <h3>Full screen video landing page</h3>
          <a href="#about" class="btn">Read More</a> -->
        </div>
      </section>  
      <AboutComponent/>
    </main>
</template>

<script>
// @ is an alias to /src
import AddressSearch from '@/components/Address.vue';
import AboutComponent from '@/components/About.vue';

export default {
  name: 'HomeView',
  components: {
    AddressSearch,
    AboutComponent
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');

/* :root {
  --primary-color: #3a4052;
} */

* {
  box-sizing: border-box;
	margin: 0;
	padding: 0;
}

main {
  font-family: 'Open Sans', sans-serif;
	line-height: 1.5;
}

main h1 {
  font-weight: 300;
	font-size: 60px;
	line-height: 1.2;
	margin-bottom: 15px;
}

.showcase {
  height: calc(100vh - 66px);
	display: flex;
	align-items: center;
	justify-content: center;
	text-align: center;
	padding: 0 20px;
}

.video-container {
  position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	overflow: hidden;
	background: url('@/assets/thumbnail.jpg') no-repeat center
  center/cover;
}

.video-container video {
  min-width: 100%;
	min-height: 100%;
  position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	object-fit: cover;
}

.video-container:after {
  content: '';
	z-index: 1;
	height: 100%;
	width: 100%;
	top: 0;
	left: 0;
	background: rgba(0, 0, 0, 0.5);
	position: absolute;
}

.content {
  z-index: 2;
}

.btn {
  display: inline-block;
	padding: 10px 30px;
	background: var(--primary-color);
	color: #fff;
	border-radius: 5px;
	border: solid #fff 1px;
	margin-top: 25px;
	opacity: 0.7;
}

.btn:hover {
  transform: scale(0.98);
}

</style>