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
    <div class="about">
      <img alt="logo" src="../assets/logo_small.png"/>
      <h1>Welcome to ZzangBaguni</h1>
      <h3>What is ZzangBaguni</h3>
      <p>
          짱바구니는 공공데이터포털에서 제공하는 한국소비자원 참가격정보서비스 API를 사용한 
          장바구니 가격 비교 서비스입니다.
      </p>  
      <h3>Used Stack</h3>
      <ul>
        <li><a href="https://vuejs.org/" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"></a></li>
        <li><a href="https://flask.palletsprojects.com/" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a></li>
        <li><a href="https://www.mongodb.com/" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white"></a></li>
      </ul>
      <h3>Find Out More</h3>  
        <div class="social">
          <a href="https://www.data.go.kr/data/3043385/openapi.do" target="_blank"><img src="https://www.data.go.kr/images/biz/DATA.ico" style="width: 48px"/></a>
          <a href="https://github.com/IdxS-dot/TEAM_LS" target="_blank" style="color: black;"><i class="bi bi-github"></i></a>
        </div>
    </div>
  </main>
</template>

<style>
h3 {
  margin: 40px 0 10px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 3px;
}
a {
  color: #42b983;
}
p {
  font-size: 1.2rem;
	max-width: 700px;
	margin: auto;
}
</style>