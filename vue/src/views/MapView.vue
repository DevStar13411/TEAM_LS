<template>
	<body>
		<main class="d-flex flex-nowrap">
			<div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-white" style="width: 300px;">
				<div class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom">
					<form  @submit="formtest"><input type="text" placeholder="키워드" id="keyword" style="width: 180px;"/>
					<button type="submit">검색하기</button>
					</form>
				</div>
				<div class="list-group list-group-flush border-bottom scrollarea">
					<div v-for="place in entp" v-bind:key="place.entpId" class="list-group-item list-group-item-action py-3 lh-sm" >
						<div class="d-flex w-100 align-items-center justify-content-between">
							  <strong class="mb-1">{{place.entpName}}</strong>
							  <small>Price</small>
						</div>
						<div class="col-10 mb-1 small">Address or Distance</div>
					  </div>
				</div>
				<!-- <div id="pagination"></div> -->
			</div>
			<div class="col">
				<div id="map"></div>			
			</div>
		</main>
	</body>

</template>

<script>
export default {
	name: 'MapView',
	data() {
		return {
			entp : [],			
			good : [],
			price : {},
			latitude: Number(this.$route.query.latitude),
			longitude: Number(this.$route.query.longitude)
		};
	},
	methods : {		
		//함수추가중 신경 x
		formtest(res){
			setTimeout(function(){
				console.log(res);//test
			},5000);
		},		
		setmarker(testdata,map,infowindow){
			var markerList=[];
			for (var i=0; i<testdata.length; i++) {
				var icon = {
						url: 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png',
						size: new window.naver.maps.Size(24, 37),
						anchor: new window.naver.maps.Point(12, 37),
						origin: new window.naver.maps.Point(0,(i * 46)+10)
					},
					marker = new window.naver.maps.Marker({
						position: new window.naver.maps.LatLng(testdata[i].latitude,testdata[i].longitude),
						map: map,
						title: testdata[i].entpName,
						//icon: icon
					});
				marker.set('seq', i);
				markerList.push(marker);
				marker.addListener('mouseover', onMouseOver);
				marker.addListener('mouseout', onMouseOut);
				icon = null; //eslint-disable-line no-unused-vars
				marker = null;
			}
			function onMouseOver(e) {
				var marker = e.overlay,
					seq = marker.get('seq');
				marker.setIcon({
					url: 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png',
					size: new window.naver.maps.Size(24, 37),
					anchor: new window.naver.maps.Point(12, 37),
					origin: new window.naver.maps.Point(0,(seq * 46)+10)
				});
				var content = '<div style="padding:5px;z-index:1;">' + marker.title+'\n price: '+ String(testdata[seq].testprice) +  '</div>';
				infowindow.setContent(content);
				infowindow.open(map, marker);
			}
			function onMouseOut(e) {
				var marker = e.overlay,
					seq = marker.get('seq'); //eslint-disable-line no-unused-vars
				marker.setIcon();
				infowindow.close();
			}
			return markerList;
		},		
		displayPlaces(places,markers,map) {
			var bounds = new window.naver.maps.LatLngBounds();
			for ( var i=0; i<places.length; i++ ) {
				// 마커를 생성하고 지도에 표시합니다
				var placePosition = new window.naver.maps.LatLng(places[i].latitude, places[i].longitude);
				// 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
				// LatLngBounds 객체에 좌표를 추가합니다
				bounds.extend(placePosition);
			}
			// 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
			map.fitBounds(bounds);
		}			
	},
	mounted() {
		let reqBody = {goods: this.$store.getters.getcartProducts, latitude: this.latitude, longitude: this.longitude};
		this.axios.post("https://zzangbaguni.shop/prices",reqBody).then((res)=>{
			this.entp = res.data.entp;
			this.good = res.data.good;
			this.price = res.data.price;
			var mapOptions = {
				//중심설정 부분 this에서 데이터 불러와서 바꿔야
				center: new window.naver.maps.LatLng(this.latitude, this.longitude),
				maxZoom: 20,
				zoom: 13,
				minZoom: 10,
				zoomControl: true,
				zoomControlOptions: {
					position: window.naver.maps.Position.TOP_RIGHT
				},
				draggable: true
			};
			var map = new window.naver.maps.Map('map',mapOptions);
			var infowindow = new window.naver.maps.InfoWindow();
			//return [testdata, map, infowindow];
			var list6 = this.setmarker(this.entp,map,infowindow);
			//this.formtest(test5[0]);
			this.displayPlaces(this.entp,list6,map);
		}).catch((err)=>{
			console.log(err);
		});
	}
};
</script>

<style>
/* .map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:600px;} */
/* #map {float:right;width:80%;height:600px;} */
#map {width:100%;height:100vh;}
/* #menu_wrap {position:fixed;top:0;left:0;bottom:10px;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;} */
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .info .price {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}
.scrollarea {
  overflow-y: auto;
}
main {
  height: 100vh;
  height: -webkit-fill-available;
  max-height: 100vh;
  overflow-x: auto;
  overflow-y: hidden;
}
body {
  min-height: 100vh;
  min-height: -webkit-fill-available;
}
</style>