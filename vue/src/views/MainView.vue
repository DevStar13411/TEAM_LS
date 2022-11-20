<template>
  <nav class="nav nav-pills nav-fill">
    <a class="nav-link category" @click="getGoodsList()"> 전체</a>
    <a class="nav-link category" @click="getGoodsList(30101)"> 정육/난류</a>
    <a class="nav-link category" @click="getGoodsList(30202)"> 수산가공품</a>
    <a class="nav-link category" @click="getGoodsList(30203)"> 낙농/축산가공품</a>
    <a class="nav-link category" @click="getGoodsList(30103)"> 생선류</a>
    <a class="nav-link category" @click="getGoodsList(30204)"> 조미료/장류/식용유</a>
    <a class="nav-link category" @click="getGoodsList(30102)"> 채소류</a>
    <a class="nav-link category" @click="getGoodsList(30205)"> 과자/빙과류</a>
    <a class="nav-link category" @click="getGoodsList(30206)"> 차/음료/주류</a>
    <a class="nav-link category" @click="getGoodsList(30301)"> 이미용품</a>
    <a class="nav-link category" @click="getGoodsList(30302)"> 세탁/주방/가사용품</a>
</nav>
    <div class="py-5">
        <div class="container text-start">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                    <div class="card">
                        <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
                        <div class="card-body">
                            <h5 class="card-title">{{item.goodName}}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{category[parseInt(item.goodSmlclsCode/1000)]}}</h6>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <button type="button" class="btn btn-sm btn-outline-secondary" @click="itemClick(item)">담기</button>
                                </div>
                                <small class="text-muted tooltip-price" @mouseover="getPriceList(item.goodId)">가격

                                  <div class="tooltip-text">
                                  <h6>가격정보</h6>
                                    <table>
                                      <thead>
                                        <th>이름</th>
                                        <th>가격</th>
                                      </thead>
                                      <tbody v-for="i in priceList[item.goodId]" v-bind:key="i.entpId">
                                        <td>{{ i.entpName }}</td>
                                        <td>{{ i.goodPrice }}</td>
                                      </tbody>
                                    </table>
                                    </div>
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
	name : 'MainView',
    data : function() {
        return {
          goodList : [],
          category : {
            30201 : "곡물가공품",
            30101 : "정육/난류",
            30202 : "수산가공품",
            30203 : "낙농/축산가공품",
            30204 : "조미료/장류/식용유",
            30102 : "채소류",
            30205 : "과자/빙과류",
            30206 : "차/음료/주류",
            30301 : "이미용품",
            30302 : "세탁/주방/가사용품",
            30103 : "생선류"},
          priceList : {}
        };

    },
    methods : {
        getGoodsList(category) {
            let get_url =  "https://zzangbaguni.shop/goods";
            if(category!==undefined){
              get_url+= "/"+category;
            }

            this.axios.get(get_url,{
                params: {
                    latitude: this.$route.query.latitude,
                    longitude: this.$route.query.longitude
                }
            }).then((res)=>{
                this.goodList = res.data.goods;
            }).catch((err) => {
                console.log(err);
            });
        },
        itemClick(item) {
            this.$router.push({name : 'GoodView', query : {itemNo : item.goodId}});
        },
        getPriceList(goodId) {
          if (this.priceList[goodId] === undefined) {
            let get_url = "https://zzangbaguni.shop/price";
            get_url += "/" + goodId;
            this.axios.get(get_url, {
              params: {
                latitude: this.$route.query.latitude,
                longitude: this.$route.query.longitude
              }
            }).then((res) => {
              this.priceList[goodId] = res.data;
            }).catch((err) => {
              console.log(err);
            });
          }
        }
    },
    mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
        this.getGoodsList();
    }
    
};
</script>

<style scoped>
.card-img-top {
  height: 15em;
  object-fit: cover;
}
.card-title {
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.4em;
  height: 2.8em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.category {
  cursor:pointer;
  border: 1px solid;
  color: black;
}

.tooltip-price .tooltip-text {
  visibility: hidden;
  width: 200px;

  background: white;
  color: black;
  border : 1px solid;
  text-align: center;
  border-radius: 6px;
  padding: 10px;

  position: absolute;
  z-index: 1;
}

.tooltip-price:hover .tooltip-text {
  visibility: visible;
}

table {

    width: 100%;
    border: 1px solid #444444;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #444444;
  }
</style>