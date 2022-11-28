<template>
		<main class="d-flex flex-nowrap">
			<div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-white" style="width: 350px;">
				<div class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom">
					<div class="app-bar"><img class="logo" src="@/assets/logo_small.png"></div>
				</div>
				<div class="list-group list-group-flush border-bottom scrollarea">
					<div v-for="place in entp" v-bind:key="place.entpId" class="list-group-item list-group-item-action py-3 lh-sm" v-on:click="vtest(place)" >
						<div class="d-flex w-100 align-items-center justify-content-between">
							<strong class="mb-1">{{place.entpName}}</strong>
							<div>
								<small class="warning-products" v-if="place.no_product !== 0">⚠️
								<div class="warning-text">없는 상품이 존재합니다.</div>
								</small>
								<strong>{{place.total_price.toLocaleString('ko-KR')+"원"}}</strong>
							</div>
						</div>
						<strong>{{place.distance/1000+"km"}}</strong>

						<div class="d-flex justify-content-end align-items-center">
							<PriceDetail v-bind:priceInfo="this.price[place.entpId]"></PriceDetail>
						</div>
					</div>
				</div>
			</div>
		<div class="col">
			<div id="map"></div>			
		</div>
	</main>
</template>

<script>

import PriceDetail from "@/components/PriceDetail";
export default {
	name: 'MapView',
  components: {PriceDetail},
  data() {
		return {
			entp : [],			
			good : [],
			price : {},
			latitude: Number(this.$route.query.latitude),
			longitude: Number(this.$route.query.longitude),
			map : {}
		};
	},
	methods : {		
		//함수추가중 신경 x
		vtest(place){
			let reqBody = {goods: this.$store.getters.getcartOnlyId, latitude: this.latitude, longitude: this.longitude};
			
			//console.log(place);
			
			this.axios.post("https://zzangbaguni.shop/prices",reqBody).then((res)=>{  //eslint-disable-line no-unused-vars
				
				var mapOptions = {
					center: new window.naver.maps.LatLng(place.latitude,place.longitude),
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
				
				
				this.setmarker(this.entp,map,infowindow);
				
				
				//console.log(place.entp);

				
			}).catch((err)=>{
				console.log(err);
			});
			
			
			
			
		},		
		setmarker(testdata,map,infowindow){
		console.log(infowindow);
			var markerList=[];
			
			var mainicon1 = {
				content: 	['<div>',
								'<div id = "infoshop";>',
									'<span style="font-size:12px">',
									testdata[0].entpName,
									'</span>',
									'</br>',
									' 💸 ',
									'<span id = "price1">', String(testdata[0].total_price.toLocaleString('ko-KR')),'원',
									'</span>',
									
								'</div>',
	'<img id="mkimg" src="https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-1024.png"  width="35" style="z-index:0"/>',
							'</div>'
								
								
								
							].join(''),
					size: new window.naver.maps.Size(38, 58),
					anchor: new window.naver.maps.Point(17.5, 35),
					
				};
			
			var marker1 = new window.naver.maps.Marker({ //eslint-disable-line no-unused-vars
				position: new window.naver.maps.LatLng(testdata[0].latitude,testdata[0].longitude),
				map: map,
				title: testdata[0].entpName,
				zIndex:2,
				icon: mainicon1
				
			});
			
			marker1.set('seq', 0);
			//window.naver.maps.Event.addListener(marker1,"click",onMouseClick);
			//window.naver.maps.Event.addListener(marker1,"mouseover",onMouseOver);
			
			//var gIcon = marker1.getIcon();
			//console.log(gIcon);
			
			marker1.addListener('mouseover', onMouseOver1);
			marker1.addListener('click', onMouseClick1);
			marker1.addListener('mouseout', onMouseOut1);
			var seqtest = marker1.get('seq');
			console.log('marker1',seqtest,marker1);
			//console.log('marker1',marker1);
	
			for (var i=1; i<testdata.length; i++) {
				
				var mainicon = {
						content: [
									'<div id = "infoshop";">',
										'<span style="font-size:12px">',
										testdata[i].entpName,
										'</span>',
										'</br>',
										' 💸 ',
										 String(testdata[i].total_price.toLocaleString('ko-KR')),'원',
										
										
									'</div>',
					'<img id="mkimg" src="https://t1.daumcdn.net/localimg/localimages/07/2018/pc/img/marker_spot.png";  width="30"; >'
									
								].join(''),
						size: new window.naver.maps.Size(38, 58),
						anchor: new window.naver.maps.Point(15, 30)
						
					};
				
				var marker = new window.naver.maps.Marker({ //eslint-disable-line no-unused-vars
					position: new window.naver.maps.LatLng(testdata[i].latitude,testdata[i].longitude),
					map: map,
					title: testdata[i].entpName,
					zIndex:1,
					icon: mainicon
					
				});
				
				
				markerList.push(marker);
				
				marker.set('seq', i);
				
				marker.addListener('mouseover', onMouseOver);
				marker.addListener('mouseout', onMouseOut);
				marker.addListener('click', onMouseClick);
				//icon = null;			 //eslint-disable-line no-unused-vars
				//marker = null;
				
			}
			console.log(markerList[3]);
			
			//console.log(markerList[1]);
			
			
			function onMouseOver1(e) {
				var marker = e.overlay;
				//var seq = marker.get('seq');
				/*marker.setIcon();
				marker.setIcon({
					content: '<img src="https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-1024.png"  width="35"/>'				
									
							,
					size: new window.naver.maps.Size(38, 58),
					anchor: new window.naver.maps.Point(19, 58),
					
				});*/
				marker.setZIndex(3);
				console.log(marker);
				//var content = '<div style="padding:5px;z-index:5;">' + marker.title+'\n price: '+ String(testdata[seq].total_price) +  '</div>';
				//infowindow.setContent(content);
				//infowindow.open(map, marker);
				//console.log(seq);
			}
			function onMouseClick1(e) {
				var marker = e.overlay;
				var seq = marker.get('seq');
				console.log("seq",seq);
				//marker.setIcon(mainicon1);
				
			
				//infowindow.close();
			}
			function onMouseOut1(e) {
				var marker = e.overlay;
				var seq = marker.get('seq');
				console.log("seq",seq);
				//marker.setIcon(mainicon1);
				marker.setZIndex(2);
				console.log(marker);
			
				//infowindow.close();
			}
			function onMouseOver(e) {
				var marker = e.overlay;
				//var seq = marker.get('seq');
				/*marker.setIcon();
				marker.setIcon({
					content: '<img src="https://t1.daumcdn.net/localimg/localimages/07/2018/pc/img/marker_spot.png"  width="30"/>'	,
					size: new window.naver.maps.Size(38, 58),
					anchor: new window.naver.maps.Point(19, 58),
					
				});*/
				marker.setZIndex(3);
				console.log(marker);
				//var content = '<div style="padding:5px;z-index:5;">' + marker.title+'\n price: '+ String(testdata[seq].total_price) +  '</div>';
				//infowindow.setContent(content);
				//infowindow.open(map, marker);
				//console.log(seq);
			}
			function onMouseClick(e) {
				var marker = e.overlay;
				var seq = marker.get('seq');
				console.log("seq",seq);
				//marker.setIcon(mainicon);
				
			
				//infowindow.close();
			}
			function onMouseOut(e) {
				var marker = e.overlay;
				var seq = marker.get('seq');
				console.log("seq",seq);
				//marker.setIcon(mainicon);
				marker.setZIndex(1);
				console.log(marker);
			
				//infowindow.close();
			}
			
			
			
			
			
			return markerList;
		},		
		displayPlaces(places,map) {
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
		},

    // this.entp에 총 가격, 가지고 있는 상품 수 체크
    calculatePrice(){
      console.log("가격",this.price);
      let productsInfo = this.$store.getters.getcartProducts;

      for(let idx in this.entp){
        let row = this.entp[idx];
        let entpId = row['entpId'];
        let total = 0; let cnt =0;

        for(let i=0;i<productsInfo.length;i++){
          let priceItem = this.price[entpId][productsInfo[i]["goodName"]];
          let QuantityItem = productsInfo[i]["goodQuantity"];
          if(!isNaN(priceItem*QuantityItem)) {
            total += priceItem * QuantityItem;
          }
          else{
            cnt++;
            this.price[entpId][productsInfo[i]["goodName"]] = "-";
          }
        }
        row["total_price"] = total;
        row["no_product"] = cnt;
      }
      this.sort_entp();
    },
    // 우선 순위 순으로 정렬
    // 1. no_product 2. total_price 3. dist
    sort_entp() {
      this.entp.sort(function (a, b) {
        if (a.no_product > b.no_product) {
          return 1;
        } else if (a.no_product < b.no_product) {
          return -1;
        }
        if (a.total_price > b.total_price) {
          return 1;
        } else if (a.total_price < b.total_price) {
          return -1;
        }
        if (a.distance > b.distance) {
          return 1;
        } else if (a.distance < b.distance) {
          return -1;
        }
      });
    },
    // 직선 거리 계산
    // calculate_dist() {
    //   for(let i in this.entp){
    //     let pos = {latitude: this.entp[i].latitude, longitude: this.entp[i].longitude};
    //     let nowPos = {latitude: this.latitude, longitude: this.longitude};
    //     this.entp[i].distance = Math.round(haversine(pos, nowPos)) / 1000;
    //   }
    // }
	},
	mounted() {
		let reqBody = {goods: this.$store.getters.getcartOnlyId, latitude: this.latitude, longitude: this.longitude};
		
		this.axios.post("https://zzangbaguni.shop/prices",reqBody).then((res)=>{
			this.entp = res.data.entp;
			this.good = res.data.good;
			this.price = res.data.price;
			console.log(this.entp);
			this.calculatePrice();
			console.log(this.entp);
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
			this.map = map;
			console.log(map);
			console.log(this.map);
			var infowindow = new window.naver.maps.InfoWindow(); 
			console.log(infowindow);
			//return [testdata, map, infowindow];
			this.setmarker(this.entp,map,infowindow);
			//this.formtest(test5[0]);
			this.displayPlaces(this.entp,map);

			
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
#infoshop {border:3px solid #0475F4; border-radius:10px /10px; padding:0px 2px;background:rgba( 255, 255, 255, 1 );font-size:10px; float:right;}
#infoshop:hover{z-index:10;color:#0475F4;}
#mkimg {z-index:0;}
#price1  {color:red;}
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
.scrollarea {
  overflow-y: auto;
}

.main {
  height: 100vh;
  height: -webkit-fill-available;
  max-height: 100vh;
  overflow-x: auto;
  overflow-y: hidden;
}

.warning-products:hover .warning-text{
  visibility: visible;
}
.warning-text{
  visibility: hidden;
  width: 70%;

  background: #FFFBE5;
  color: black;
  border : 1px solid ;

  text-align: center;
  border-radius: 6px;
  padding: 10px;
  top:50px;
  right :10px;
  position: absolute;
  z-index: 1;
}

PriceDetail{
  text-align:right;
}
</style>