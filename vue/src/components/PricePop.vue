<template>
    <small class="text-muted tooltip-price" @mouseover="getPriceList(goodId)">가격
        <div class="tooltip-text">
            <h6>가격정보</h6>
            <table>
                <thead>
                <th>이름</th>
                <th>가격</th>
                </thead>
                <tbody v-for="i in priceList[goodId]" v-bind:key="i.entpId">
                <td>{{ i.entpName }}</td>
                <td>{{ i.goodPrice }}</td>
                </tbody>
            </table>
        </div>
    </small>
</template>

<script>
export default {
	name : 'PricePop',
    data : function() {
        return {
            priceList : {}          
        };
    },
    props:{
        goodId: Number
    },
    methods : {
        getPriceList(goodId) {
            if (this.priceList[goodId] === undefined) {
                let get_url = "https://zzangbaguni.shop/price";
                get_url += "/" + goodId;
                this.axios.get(get_url, {
                params: {
                    latitude: this.$route.query.latitude,
                    longtitude: this.$route.query.longtitude
                }
                }).then((res) => {
                this.priceList[goodId] = res.data;
                }).catch((err) => {
                console.log(err);
                });
            }
        }
    }    
};
</script>

<style>
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
</style>