<template>
  <!-- @submit.prevent == e.preventDefault() -->
  <form @submit.prevent="predict">
    <h3>Testing probability prediction</h3>

    <!-- v-model is a two-way binding 
         to a reactive variable in data -->
    <input v-model="age" type="text" placeholder="age..">
    <input v-model="income" type="text" placeholder="income..">
    <br>
    <button>test</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      age: '',
      income: '',
    }
  },
  methods: {
    async predict(e) {
      // e.preventDefault()

      let values = {
        age: this.age,
        income: this.income
      }

      let res = await fetch('/api/predict', {
        method: 'POST',
        body: JSON.stringify(values)
      })

      let prediction = await res.json()

      // call mutation in store to change a state variable
      this.$store.commit('setPrediction', prediction)

      console.log(prediction) // debug
    }
  },
  // on component creation, but before rendering
  created() {
    
  }
}
</script>

<style scoped>

</style>