<template>
    <small class="text-muted tooltip-detail">자세히
        <div class="tooltip-detail-text">
            <h6>가격정보</h6>
            <table>
                <thead>
                <th>이름</th>
                <th>가격</th>
                </thead>
                <tbody v-for="(price,name) in this.priceInfo" :key="name">
                <td>{{ name }}</td>
                <td>{{ price }}</td>
                </tbody>
            </table>
        </div>
    </small>
</template>

<script>
export default {
	name : 'PriceDetail',
    props:
        ["priceInfo"]
};
</script>

<style>
.tooltip-detail-text {
  visibility: hidden;
  width: 70%;

  background: white;
  color: black;
  border : 1px solid;

  text-align: center;
  border-radius: 0px;
  padding: 10px;
  top: 85px;
  right:10px;
  position: absolute;
  z-index: 1;
}

.tooltip-detail:hover .tooltip-detail-text {
  visibility: visible;
}


table {

    width: 100%;
    border: 1px solid #444444;
    border-collapse: collapse;
    text-align: center;
  }
  th, td {
    border: 1px solid #444444;
  }

</style>