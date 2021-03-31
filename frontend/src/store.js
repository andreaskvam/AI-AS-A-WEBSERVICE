import { createStore } from 'vuex'

// this.$store.state.prediction
const state = {
  prediction: {
    willClick: false,
    probability: 0
  }
}

// this.$store.commit('setPrediction', prediction)
const mutations = {
  setPrediction(state, prediction) {
    state.prediction = prediction
  }
}

export default createStore({ state, mutations })