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
    name : 'MapView'
};
</script>

<style scoped>
.board { width:800px; margin: 20px auto; }
</style>