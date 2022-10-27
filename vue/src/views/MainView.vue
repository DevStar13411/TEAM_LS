<template>
    <div class="board">
        <h1>This is Main View</h1>
        <table>
            <colgroup>
				<col style="width:20%">
				<col style="width:*">
				<col style="width:25%">
			</colgroup>
            <thead>
                <tr>
                    <th>상품번호</th>
                    <th>상품명</th>
                    <th>상품코드</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in goodList" v-bind:key="item.goodId">
                    <td>{{item.goodId}}</td>
                    <td>{{item.goodName}}</td>
                    <td>{{item.goodSmlclsCode}}</td>
                </tr>
            </tbody>
        </table>
	</div>
</template>

<script>
export default {
	name : 'MainView',
    data : function() {
        return {
            goodList : []
        };
    },
    methods : {
        getGoodsList() {
            //this.axios.get("http://localhost:5000/goods",{
            this.axios.get("http://43.200.162.158/goods",{
                params: {
                    address: this.$route.query.address,
                    latitude: this.$route.query.latitude,
                    longtitude: this.$route.query.longtitude
                }
            }).then((res)=>{
                console.log(res);
                this.goodList = res.data;
            }).catch((err) => {
                console.log(err);
            });
        },
    },
    mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
        this.getGoodsList();
    }
    
};
</script>

<style scoped>
.board { width:600px; margin: 20px auto; }
.board { width:600px; margin: 20px auto; }
.board table { width:100%; border-top:2px solid #1d4281; border-spacing:0; }
.board table th { padding:8px 10px 10px 10px; vertical-align:middle; color:#1d4281; font-size:14px; border-bottom:1px solid #ccc; background:#f8f8f8; }
.board table td { padding:7px 10px 9px 10px; text-align:center; vertical-align:middle; border-bottom:1px solid #ccc; font-size:14px; line-heighT:150%; }
</style>