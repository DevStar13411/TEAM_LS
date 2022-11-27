<template>
      <section id="about">
        <h1>About</h1>
        <p>
          짱바구니는 공공데이터포털에서 제공하는 한국소비자원 참가격정보서비스 API를 사용한 
          장바구니 가격 비교 서비스입니다.
        </p>  
        <h2>Find Out More</h2>  
        <div class="social">
          <a href="https://www.data.go.kr/data/3043385/openapi.do" target="_blank"><img src="https://www.data.go.kr/images/biz/DATA.ico" style="width: 48px"/></a>
          <a href="https://github.com/IdxS-dot/TEAM_LS" target="_blank"><i class="bi bi-github"></i></a>
        </div>
      </section>
</template>

<script>
export default {
  name: 'AboutComponent'
};
</script>

<style>
#about {
	padding: 40px;
	text-align: center;
  color: #3a4052;
}

#about a{
  text-decoration: none;
  color: #3a4052;
}

#about p {
  font-size: 1.2rem;
	max-width: 700px;
	margin: auto;
}

#about h2 {
  margin: 30px 0;
	color: var(--primary-color);
  font-weight: bold;
}

.social a {
  margin: 0 5px;
}

.social i {
  font-size: 3rem;
  vertical-align: middle;
}
</style>