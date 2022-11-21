<template>
  <main>

<div id="map" style="width:80%;height:600px;float:right;"></div>
  <div class="map_wrap">
    <div id="menu_wrap" class="bg_white">
      <div class="option">
        <div>
          <form onsubmit="searchPlaces(); return false;">
            키워드 : <input type="text" placeholder="test" id="keyword" size="15" />
            <button type="submit">검색하기</button>
          </form>
        </div>
      </div>
      <hr>
      <ul id="placesList"></ul>
      <div id="pagination"></div>
    </div>
    <div id="inputbtn">
      <input type="text" name="testplace" id="testplace" placeholder="장소입력" onchange="iptest()" />
      <input type="button"  value="입력" onclick="" />
      <input type="button" id="bttest" value="현위치로 설정" onclick="" />
    </div>
  </div>
  </main>

</template>

<script>
export default {
  name: 'MapView',
  data() {
    return {
      entp : [],
      good : [],
      price : []
    };
  },
  methods: {
    getPrices() {
      let get_url =  "https://zzangbaguni.shop/prices";

      // type이 str으로 고정되는 현상이 있어 강제 형변환 필요
      let goods = this.$route.query.goods;
      let goods_int = goods.map(function (x) {
        return parseInt(x, 10);
      });
      let data = {
          latitude: parseFloat(this.$route.query.latitude),
          longitude: parseFloat(this.$route.query.longitude),
          goods: goods_int
      };

      this.axios.post(get_url,data).then((res)=>{
        this.entp = res.data.entp;
        this.good = res.data.good;
        this.price = res.data.price;

      }).catch((err) => {
        console.log(err);
      });
    },

    // 다른 함수나 디테일은 별도로 추가 부탁바랍니다.
    getMap() {
      var mapOptions = {
        // center: new naver.maps.LatLng(avglat, avglng),
        maxZoom: 20,
        zoom: 13,
        minZoom: 10,
        zoomControl: true,
        zoomControlOptions: {
          position: window.naver.maps.Position.TOP_RIGHT
        }
      };
      new window.naver.maps.Map('map',mapOptions);
    }
  },
  mounted() {
    this.getPrices();
    this.getMap();
  }
};

</script>

