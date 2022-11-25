<template>
<main>
	<div class="map_wrap">
		<div id="map" ></div>
		<div class="map_wrap">
			<div id="menu_wrap" class="bg_white">
				<div class="option">
					<div>
						<form  @submit="formtest"> 키워드 : <input type="text" placeholder="test" id="keyword" size="15" />
						<button type="submit">검색하기</button>
						</form>
					</div>
				</div>
				<hr>
				<ul id="placesList"></ul>
				<div id="pagination"></div>
			</div>
		</div>
	</div>
</main>

</template>

<script>
export default {
	name: 'MapView',
	data() {
		return {
			//test용으로 entp값넣어둠
			entp : [{ "entpId": 33, "entpName": "(주)농협하나로유통 수원점", "latitude": 37.283010817525, "longitude": 126.966701882092}],
			
			good : [],
			price : [],
			lat : 0,
			lng : 0
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
			console.log(this.entp); //then 밖에서 변경되었는지 테스트
		},

		getMap() {
			//현재 이 밑에 주석된 코드에서 testdata대신 this의 값을 받아 올 수 있게 만들어야
			/*for (var i=0; i<testdata.length; i++) {
				testdata[i].latitude=Number(testdata[i].latitude.toFixed(6));
				testdata[i].longitude=Number(testdata[i].longitude.toFixed(6));
				
				this.lat+=testdata[i].latitude;
				this.lng+=testdata[i].longitude;
				
			}
			this.lat/=testdata.length;
			this.lng/=testdata.length;

			this.lat=Number(this.lat.toFixed(6));
			this.lng=Number(this.lng.toFixed(6));
			*/
			var mapOptions = {
				//중심설정 부분 this에서 데이터 불러와서 바꿔야
				//center: new naver.maps.LatLng(this.lat, this.lng),
				maxZoom: 20,
				zoom: 13,
				minZoom: 10,
				zoomControl: true,
				zoomControlOptions: {
					position: window.naver.maps.Position.TOP_RIGHT
				}
			};
			new window.naver.maps.Map('map',mapOptions);
			console.log(this.entp);//test
		},
		
		//함수추가중 신경 x
		formtest(){
			console.log(this.lng);//test
		},
		getcenter(){
			/*for (var i=0; i<testdata.length; i++) {
				testdata[i].latitude=Number(testdata[i].latitude.toFixed(6));
				testdata[i].longitude=Number(testdata[i].longitude.toFixed(6));
				
				this.lat+=testdata[i].latitude;
				this.lng+=testdata[i].longitude;
				
			}
			this.lat/=testdata.length;
			this.lng/=testdata.length;

			this.lat=Number(this.lat.toFixed(6));
			this.lng=Number(this.lng.toFixed(6));
			*/

		},
		setmarker(){
			var markerList=[];
			/*for (var i=0; i<testdata.length; i++) {
				var icon = {
						url: 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png',
						size: new window.naver.maps.Size(24, 37),
						anchor: new window.naver.maps.Point(12, 37),
						origin: new window.naver.maps.Point(0,(i * 46)+10)
					},
					marker = new window.naver.maps.Marker({
						position: new window.naver.maps.LatLng(testdata[i].latitude,testdata[i].longitude),
						map: map,
						title: testdata[i].entpName
						//icon: icon
					});
				marker.set('seq', i);

				markerList.push(marker);

				marker.addListener('mouseover', onMouseOver);
				marker.addListener('mouseout', onMouseOut);
				icon = null;
				marker = null;
			}*/
			markerList.push("testtest");
		},
		//infowindow 관련 서로 변수가 엮이고 밖에 변수설정이 되어있는 경우가 많아서 정리 필요
		/*displayinfo(){
			function onMouseOver(e) {
				var marker = e.overlay,
					seq = marker.get('seq');

				marker.setIcon({
					url: 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png',
					size: new window.naver.maps.Size(24, 37),
					anchor: new window.naver.maps.Point(12, 37),
					origin: new window.naver.maps.Point(0,(seq * 46)+10)
				});
				displayInfowindow(marker,marker.title,seq);
			}

			function onMouseOut(e) {
				var marker = e.overlay,
					seq = marker.get('seq');
				marker.setIcon();
				infowindow.close();
			}
			function displayInfowindow(marker, title, seq) {
				
				var content = '<div style="padding:5px;z-index:1;">' + title+'\n price: '+ String(testdata[seq].testprice) +  '</div>';

				infowindow.setContent(content);
				infowindow.open(map, marker);
			}
		},*/
		//리스트에 결과값 넣기 데이터받아서 수정필요
		/*setlist(){
			function displayPlaces(places,markers) {
				var listEl = document.getElementById('placesList'), 
				menuEl = document.getElementById('menu_wrap'),
				fragment = document.createDocumentFragment(), 
				bounds = new window.naver.maps.LatLngBounds(), //네이버로바꾸기
				listStr = '';
				
				// 검색 결과 목록에 추가된 항목들을 제거합니다
				removeAllChildNods(listEl);

				// 지도에 표시되고 있는 마커를 제거합니다
				//removeMarker(markers);
				
				for ( var i=0; i<places.length; i++ ) {

					// 마커를 생성하고 지도에 표시합니다
					var placePosition = new window.naver.maps.LatLng(places[i].latitude, places[i].longitude),
						//marker = addMarker(placePosition, i), 
						itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

					// 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
					// LatLngBounds 객체에 좌표를 추가합니다
					bounds.extend(placePosition);

					// 마커와 검색결과 항목에 mouseover 했을때
					// 해당 장소에 인포윈도우에 장소명을 표시합니다
					// mouseout 했을 때는 인포윈도우를 닫습니다
					
					fragment.appendChild(itemEl);
				}

				// 검색결과 항목들을 검색결과 목록 Element에 추가합니다
				listEl.appendChild(fragment);
				menuEl.scrollTop = 0;

				// 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
				map.setBounds(bounds);
			}
			
			function getListItem(index, places) {

				var el = document.createElement('li'),
				itemStr = '<span class="markerbg marker_' + String(index+1) + '"></span>' +'<div class="info">' +'   <h5>' + places.entpName + '</h5>';

				if (places.road_address_name) {
					itemStr += '    <span>' + places.road_address_name + '</span>' +
								'   <span class="jibun gray">' +  places.address_name  + '</span>';
				} 
				else {
					itemStr += '    <span>' +  places.address_name  + '</span>'; 
				}
							 
				//itemStr += '  <span class="tel">' + places.phone  + '</span>' +'</div>';
				itemStr += '  <span class="price">' + places.testprice  + '</span>' + '</div>';

				el.innerHTML = itemStr;
				el.className = 'item';

				return el;
			}
			
			function removeAllChildNods(el) {   
				while (el.hasChildNodes()) {
					el.removeChild (el.lastChild);
				}
			}
		}*/
	},
	created(){
		this.getPrices();
	},
	mounted() {
		//this.getcenter();
		
		this.getMap();
	}
};

</script>

<style>
.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:600px;}
#map {float:right;width:80%;height:600px;}
#menu_wrap {position:fixed;top:0;left:0;bottom:10px;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
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

</style>

