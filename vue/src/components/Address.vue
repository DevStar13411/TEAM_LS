<template>
  <div>
    <div>
      <div class="search">
        <input type="text" placeholder="도로명 주소 검색하기" @click="showApi">
        <i class="bi bi-search" style="cursor: pointer;" @click="showApi"></i>
      </div>
      <div class="my-2">
        <a href="#" @click="geofind" style="font-size: 14px; color: #42b983;">현재 위치를 주소지로 설정</a>
      </div>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'AddressSearch',
  data() {
    return {
      addr: '',
      latitude: '',
      longitude: '',
    };
  },
  methods: {

    showApi() {
      new window.daum.Postcode({
        oncomplete: (data) => {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            let fullRoadAddr = data.roadAddress; // 도로명 주소 변수
            let extraRoadAddr = ''; // 도로명 조합형 주소 변수

            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '' && data.apartment === 'Y'){
              extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }
            // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
            if(fullRoadAddr !== ''){
                fullRoadAddr += extraRoadAddr;
            }

            // 주소 정보를 해당 필드에 넣는다.
            this.addr = fullRoadAddr;

            this.axios.get("https://zzangbaguni.shop/coordinates",{
                params: {
                  address: this.addr
                }
            }).then((res)=>{
                this.latitude = res.data.latitude;
                this.longitude = res.data.longitude;
                this.$router.push({name: 'MainView', query: {latitude: this.latitude, longitude: this.longitude}});
            }).catch((err) => {
                console.log(err);
            });

        }
      //}).embed(this.$refs.embed) //팝업 띄우기 어려운 모바일 환경일 경우 embed로 띄우기도 가능
      }).open();

    },//참고: https://chlost.tistory.com/53
    geofind() {
      if(!("geolocation" in navigator)) {
        this.textContent = 'Geolocation is not available.';
        return;
      }
      this.textContent = 'Locating...';
            
      // get position
      navigator.geolocation.getCurrentPosition(pos => {
      this.latitude = pos.coords.latitude;
      this.longitude = pos.coords.longitude;
      this.$router.push({name: 'MainView', query: {latitude: this.latitude, longitude: this.longitude}});
      });
    }//참고: https://e-una.tistory.com/7

  }
};
</script>

<style>
.search {
  position: relative;
  width: 300px;
  margin: auto;
}

.search input {
  width: 100%;
  border: 1px solid #bbb;
  border-radius: 8px;
  padding: 10px 12px;
  font-size: 16px;
}

.search i {
  position : absolute;
  width: 17px;
  top: 10px;
  right: 12px;
  margin: 0;
}
</style>
