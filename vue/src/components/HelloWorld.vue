<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      <input placeholder="도로명 주소 검색하기"><input type="button" value="검색"><br>
      현재 위치를 주소지로 설정(<a href="https://business.juso.go.kr/addrlink/openApi/apiExprn.do" target="_blank" rel="noopener">도로명 주소 API</a>)
    </p>
    <h3>Used Stack</h3>
    <ul>
      <li><a href="https://vuejs.org/" target="_blank" rel="noopener">Vue.js</a></li>
      <li><a href="https://www.nginx.com/" target="_blank" rel="noopener">Nginx</a></li>
      <li><a href="https://gunicorn.org/" target="_blank" rel="noopener">Gunicorn</a></li>
      <li><a href="https://flask.palletsprojects.com/" target="_blank" rel="noopener">Flask</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
